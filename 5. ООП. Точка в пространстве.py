from math import sqrt


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        if isinstance(other, Point3D):
            return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
        else:
            raise ValueError

p1 = [-74.47220433185721, 33.7341005642194, -77.5037737985927]
p2 = [-47.735349609428624, -76.5908841887246, -20.063098551336765]
point1 = Point3D(*p1)
point2 = Point3D(*p2)
print(point1.distance('test'))
# >>> {ValueError}test
# print(point1.distance(point2))
# >>> 127.22379036189065