import math

class Vector2f:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.connected = False

    def __repr__(self):
        return repr((self.x, self.y))

    def get(self):
        return (self.x, self.y)

    def dot(self, vecB):
        return self.x * vecB.x + self.y * vecB.y

    def mod2(self):
        return self.dot(self)

    def mod(self):
        return math.sqrt(self.mod2())

    def norm(self):
        m = self.mod()
        if m != 0:
            return Vector2f(self.x / m, self.y / m)
        else:
            return Vector2f(0, 0)

    def angleTo(self, other):
        return math.acos(self.dot(other) / (self.mod() * other.mod()))

    def flip(self):
        return Vector2f(-self.x, -self.y)

    def setMagnitude(self, m):
        return self.norm().mulS(m)

    def set(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        return Vector2f(x, y)

    def rotate(self, theta):
        cos = math.cos(theta)
        sin = math.sin(theta)
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector2f(x, y)

    def mulS(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector2f(x, y)

    def add(self, vecB):
        x = self.x + vecB.x
        y = self.y + vecB.y
        return Vector2f(x, y)

    def sub(self, vecB):
        x = self.x - vecB.x
        y = self.y - vecB.y
        return Vector2f(x, y)

    def mul(self, vecB):
        x = self.x * vecB.x
        y = self.x * vecB.y
        return Vector2f(x, y)

    def perpendicular(self):
        return Vector2f(self.y, -self.x)

    def isConnected(self):
        return self.connected

    def setConnected(self, connected):
        self.connected = connected

    def getGradient(self):
        if self.x != 0:
            return self.y / self.x
        else:
            return 0

    def equals(self, pos):
        if pos.x == self.x and pos.y == self.y:
            return True
        else:
            return False
