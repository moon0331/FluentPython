from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r %r)' % (self.x, self.y)
        # 문자열 명확해야, 가능하면 표현된 객체를 재생성하는 데 필요한 소스와 동일해야
        # __repr__ vs __str__ : 둘중 하나만 구현해야 한다면 __repr__ 구현해라
        # __str__ 구현 안되어 있으면 __repr__을 호출
        # https://bit.ly/1Vm7j1N

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1+v2)
v = Vector(3, 4)
print(abs(v))

print(v*3)
print(abs(v*3))