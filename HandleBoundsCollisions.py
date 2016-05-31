from Vector2f import *
from Particle import *


class VectorEqn:

    def __init__(self, s, d):
        self.s = s
        self.d = d

    def calc(self, k):
        return self.s.add(self.d.mulS(k))

def calculateRoots(a, b, c):
    t1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    t2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)

    return (t1, t2)

def calculateQuadraticCoefs(p, boundFunction):
    x = boundFunction.s
    y = boundFunction.d

    ymod2 = y.mod2()
    k1 = y.dot(p.s.sub(x)) / ymod2
    k2 = p.v.dot(y) / ymod2

    fk1 = boundFunction.calc(k1)

    a = k2*k2*ymod2 -2*k2*p.v.dot(y) + p.v.mod2()
    b = 2*k2*fk1.dot(y) - 2*(k2*p.s.dot(y) + fk1.dot(p.v)) + 2*p.v.dot(p.s)
    c = fk1.mod2() - 2*p.s.dot(fk1) + p.s.mod2() - p.r*p.r

    return (a, b, c);

## wall is a 2-tuple (a, b) of Vector2fs describing the line in 2d, a + kb
def handleCollisionWithWall(p, boundFunction, delta, cR):
    (a, b, c) = calculateQuadraticCoefs(p, boundFunction)
    if b*b - 4*a*c >= 0 and a != 0:
        (t1, t2) = calculateRoots(a, b, c)
        t = min(t1, t2)

        if 0 < t and t <= delta:
            p.s = p.s.add(p.v.mulS(t))

            n = boundFunction.d.perpendicular()

            alpha = p.v.flip().angleTo(n)
            beta = p.v.angleTo(n)

            v = p.v.rotate(beta - alpha)
            dv = v.sub(p.v);
            p.applyForce(n.mulS(dv.mod() * p.m / delta))

def hanleBoundsCollisions(p, bounds, delta, cR):#
    (w, h) = bounds
    d1 = Vector2f(-1, 0)
    d2 = Vector2f(0, 1)
    d3 = Vector2f(1, 0)
    d4 = Vector2f(0, -1)

    s1 = Vector2f(0, 0)
    s2 = Vector2f(w, h)

    handleCollisionWithWall(p, VectorEqn(s1, d1), delta, cR)
    handleCollisionWithWall(p, VectorEqn(s1, d2), delta, cR)
    handleCollisionWithWall(p, VectorEqn(s2, d3), delta, cR)
    handleCollisionWithWall(p, VectorEqn(s2, d4), delta, cR)
