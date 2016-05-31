from Particle import *
from HandleParticleCollisions import handleCollisionWithParticle
from HandleBoundsCollisions import hanleBoundsCollisions
from LineSegAlg import IntersectionFinder
import Renderer
import random


def segmentIsHorizontal(seg):
    (p1, p2) = seg
    (x1, y1) = p1
    (x2, y2) = p2
    return y1 == y2

class ParticleSystem:

    def __init__(self, width, height):
        self.particles = []

        ## bounds is a 2 tuple (width, height)
        self.bounds = (width, height)

        ## Coef of restitution
        self.cR = 1

    def getStationaryParticles(self):
        stationary = []
        for p in self.particles:
            if p.v.get() == (0, 0):
                stationary.append(p)
        return stationary

    def getMovingParticles(self):
        moving = []
        for p in self.particles:
            if p.v.get() != (0, 0):
                moving.append(p)
        return moving;

    def getSegmentParticlePairs(self, delta):
        segmentParticlePairs = []

        for p in self.particles:
            if p.v.get() != (0, 0):
                s1 = p.s.get()
                s2 = p.s.add(p.v.mulS(delta)).get()
                seg = (s1, s2)

                if segmentIsHorizontal(seg):
                    print(seg, "is horizontal.")
                segmentParticlePairs.append((seg, p))

        return segmentParticlePairs

    def update(self, delta):
        # stationaryParticles = self.getStationaryParticles()
        # movingParticles = self.getMovingParticles()
        # for s in stationaryParticles:
        #     for m in movingParticles:
        #         handleCollisionWithParticle(s, m, delta, self.cR)

        #print(len(stationaryParticles))

        # segmentParticlePairs = self.getSegmentParticlePairs(delta)
        # #print(len(segmentParticlePairs))
        # finder = IntersectionFinder(segmentParticlePairs)
        #
        # for intersection in finder:
        #     (seg1, p1) = intersection[0]
        #     (seg2, p2) = intersection[1]
        #     handleCollisionWithParticle(p1, p2, delta, self.cR)

        for p in self.particles:
            # hanleBoundsCollisions(p, self.bounds, delta, self.cR)
            p.update(delta)

        l = len(self.particles)
        for i in range(0, l):
            p1 = self.particles[i]
            hanleBoundsCollisions(p1, self.bounds, delta, self.cR)
            for j in range(i, l):
                p2 = self.particles[j]
                handleCollisionWithParticle(p1, p2, delta, self.cR)

#    def update(self, delta):
#        self.handleCollisions(delta)
#        for p in self.particles:
#            p.update(delta)

    def addParticle(self):
        hasAdded = False
        (w, h) = self.bounds
        r = random.randint(20, 30)
        x = random.randint(int(r), int(w - r))
        y = random.randint(int(r), int(h - r))

        p = Particle(x, y, r)
        fx = 10000*random.randint(-100000, 100000)
        fy = 10000*random.randint(-100000, 100000)
        p.applyForce(Vector2f(fx, fy))
        self.particles.append(p)
        return True
