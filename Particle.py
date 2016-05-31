from Vector2f import Vector2f
import math

class Particle:

    def __init__(self, x, y, r):
        self.s = Vector2f(x, y)
        self.v = Vector2f(0, 0)
        self.a = Vector2f(0, 0)
        self.f = Vector2f(0, 0)
        self.m = (4/3) * math.pi * r * r * r
        self.r = r
        self.trail = []
        self.showTrail = False

    def setShowTrail(self, showTrail):
        self.showTrail = showTrail

    def update(self, delta):
        self.a = self.f.mulS(1 / self.m)
        self.v = self.v.add(self.a.mulS(delta))
        # print(self.v.x, self.v.y, delta)
        self.s = self.s.add(self.v.mulS(delta))
        self.f = Vector2f(0, 0)

        if self.showTrail:
            self.trail.append(self.s)
            if len(self.trail) > 10:
                self.trail.pop(0)

    def applyForce(self, f):
        self.f = self.f.add(f)
