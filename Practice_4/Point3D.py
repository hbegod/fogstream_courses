# напишите реализацию класса Point3D
import math


class Point3D:
    """
    class Point3D
    input coordinates:
    x
    y
    z
    methods:
    distance - distance to other point object
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        if not isinstance(other, Point3D):
            raise ValueError('В метод передан параметр неверного типа. '
                             'Тип должен быть Point3D'
                             )
        return math.sqrt(math.pow(other.x - self.x, 2) +
                         math.pow(other.y - self.y, 2) +
                         math.pow(other.z - self.z, 2)
                         )
