from queue import PriorityQueue
from bintrees import FastRBTree
import math

################################################################################

TOP             = 0
BOTTOM          = 1
INTERSECTION    = 2

class EventPoint:

    def __init__(self, eventType, point, objs):
        self.point = point
        self.type = eventType
        self.objs = objs

    def key(self):
        (x, y) = self.point
        return -y

    def __lt__(self, other):
        return self.key() < other.key()

    def __le__(self, other):
        return self.key() <= other.key()

    def __eq__(self, other):
        return self.key() == other.key()

    def __ge__(self, other):
        return self.key() >= other.key()

    def __gt__(self, other):
        return self.key() > other.key()

    def __ne__(self, other):
        return self.key() != other.key()

################################################################################

def order(segment):
    (p1, p2) = segment
    (x1, y1) = p1
    (x2, y2) = p2
    return segment if y1 > y2 else (p2, p1)

def segmentYCoords(segment):
    (p1, p2) = order(seg)
    (x1, y1) = p1
    (x2, y2) = p2
    return (y1, y2)

def initEventPoints(segmentObjectPairs):
    eventPoints = PriorityQueue()

    for (seg, obj) in segmentObjectPairs:
        orderedSeg = order(seg)
        pair = (orderedSeg, obj)
        (p1, p2) = orderedSeg
        ep1 = EventPoint(TOP, p1, [pair])
        ep2 = EventPoint(BOTTOM, p2, [pair])
        eventPoints.put((ep1.key(), ep1))
        eventPoints.put((ep2.key(), ep2))

    return eventPoints

def intersect(seg1, seg2):
    (p1a, p1b) = seg1
    (p2a, p2b) = seg2

    (x1a, y1a) = p1a
    (x1b, y1b) = p2b
    (x2a, y2a) = p2a
    (x2b, y2b) = p2b

    if y1a-y1b == 0 or y2a-y2b == 0:
        return None

    m1 = (y1a-y1b) / (x1a-x1b)
    c1 = y1a - m1*x1a
    m2 = (y2a-y2b) / (x2a-x2b)
    c2 = y2a - m2*x2a

    if m1 - m2 == 0:
        return None

    x = (c1 - c2) / (m2 - m1)
    y = m1*x + c1

    cond1 = max(x1a,x1b) >= x and x >= min(x1a,x1b)
    cond2 = max(y1a,y1b) >= y and y >= min(y1a,y1b)

    if cond1 and cond2:
        return (x, y)

    return None

def swap(tree, k1, k2):
    v1 = tree.get_value(k1)
    v2 = tree.get_value(k2)
    tree.remove(k1)
    tree.remove(k2)
    tree.insert(k1, v2)
    tree.insert(k2, v1)


def isSegmentAPoint(seg):
    (p1, p2) = seg
    return p1 == p2

################################################################################

class IntersectionFinder:

    def __init__(self, segmentObjectPairs):
        self.eventPoints = initEventPoints(segmentObjectPairs)
        self.status = FastRBTree() #initSweepStatus(eventPoints)

    def __iter__(self):
        return self

    def __next__(self):
        while not self.eventPoints.empty():
            (y, ep) = self.eventPoints.get()
            (seg0, obj0) = ep.objs[0]
            #epType = "top" if ep.type == TOP else "bottom" if ep.type == BOTTOM else "intersection"
            #print(seg0, epType, isSegmentAPoint(seg0))

            if ep.type == TOP:
                self.status.insert(seg0, ep.objs[0])
                try:
                    succ = self.status.succ_item(seg)
                    (seg1, obj1) = succ
                    p = intersect(seg0, seg1)
                    if p != None:
                        newEp = EventPoint(INTERSECTION, p, ep.objs+[succ])
                        eventPoints.put((newEp.key(), newEp))
                except Exception:
                    pass
                try:
                    prev = self.status.prev_item(seg)
                    (seg1, obj1) = prev
                    p = intersect(seg0, seg1)
                    if p != None:
                        newEP = EventPoint(INTERSECTION, p, [prev]+ep.objs)
                        eventPoints.put((newEp.key(), newEp))
                except Exception:
                    pass

            elif ep.type == BOTTOM:
                try:
                    prev = self.status.prev_item(seg0)
                    succ = self.status.succ_item(seg0)
                    (seg1, obj1) = succ
                    (seg2, obj2) = prev
                    p = intersect(seg1, seg2)
                    if p != None:
                        newEp = EventPoint(INTERSECTION, p, [prev, succ])
                        eventPoints.put((newEp.key(), newEp))
                except Exception:
                    pass
                self.status.remove(seg0)

            elif ep.type == INTERSECTION:
                prev = self.status.get_value(seg0)
                succ = self.status.succ_item(seg0)
                (seg1, obj1) = succ
                (seg2, obj2) = prev
                swap(self.status, seg1, seg2)

                try:
                    succc = self.status.succ_item(seg1)
                    (seg3, obj3) = succc
                    p = intersect(seg1, seg3)
                    if p != None:
                        newEp = EventPoint(INTERSECTION, p, [succ, succc])
                        eventPoints.put((newEp.key(), newEp))
                except Exception:
                    pass
                try:
                    prevv = self.status.prev_item(seg2)
                    (seg4, obj4) = prevv
                    p = intersect(seg2, seg4)
                    if p != None:
                        newEp = EventPoint(INTERSECTION, p, [prevv, prev])
                        eventPoints.put((newEp.key(), newEp))
                except Exception:
                    pass

                return ep.objs


        raise StopIteration
