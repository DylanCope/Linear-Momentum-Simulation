from Vector2f import *
from Particle import *

def calculateQuadraticCoefs(p1, p2):
    ## See working for collision of circles moving between frames
    dS = p1.s.sub(p2.s)
    dV = p1.v.sub(p2.v)
    sR = p1.r + p2.r

    ## at^2 + bt + c = 0
    a = dV.mod2()
    b = 2 * dS.dot(dV)
    c = dS.mod2() - sR*sR

    return (a, b, c)

def calculateRoots(a, b, c):
    t1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    t2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)

    return (t1, t2)

def momentumCalculation(p1, p2, cR):
    (u1x, u1y) = p1.v.get()
    (u2x, u2y) = p2.v.get()
    m1 = p1.m
    m2 = p2.m
    s = m1 + m2

    vx = (m1*u1x + m2*u2x + m2*cR*(u1x - u2x)) / s
    vy = (m1*u1y + m2*u2y + m2*cR*(u1y - u2y)) / s

    return Vector2f(vx, vy)

def applyCollisionForces(p1, p2, cR, delta):

    v1 = momentumCalculation(p2, p1, cR)
    v2 = momentumCalculation(p1, p2, cR)

    f1 = v1.sub(p1.v).mulS(p1.m / delta)
    f2 = v2.sub(p2.v).mulS(p2.m / delta)

    p1.applyForce(f1)
    p2.applyForce(f2)

## Calculates and sets the new positions and force on the particles
## if they have collided
def handleCollisionWithParticle(p1, p2, delta, cR):

    ## Apply relevant mathematics regarding collision
    (a, b, c) = calculateQuadraticCoefs(p1, p2)

    if b*b - 4*a*c >= 0 and a != 0:
        (t1, t2) = calculateRoots(a, b, c)
        t = min(t1, t2)

        if 0 < t and t <= delta:

            ## Apply s = s0 + vt to move particles to where they collide
            p1.s = p1.s.add(p1.v.mulS(t))
            p2.s = p2.s.add(p2.v.mulS(t))

            applyCollisionForces(p1, p2, cR, delta)
