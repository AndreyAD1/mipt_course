from functools import reduce
from typing import List


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, addend):
        new_x = self.x + addend.x
        new_y = self.y + addend.y
        return Vector(new_x, new_y)

    def __sub__(self, subtrahend):
        return Vector(self.x - subtrahend.x, self.y - subtrahend.y)

    def __str__(self):
        return 'Vector x={}, y ={}'.format(self.x, self.y)

    def __mul__(self, multiplier):
        return Vector(self.x * multiplier.x, self.y * multiplier.y)

    def __rmul__(self, multiplier):
        return Vector(self.x * multiplier.x, self.y * multiplier.y)

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        return self


def get_center_of_mass(points: List[Vector]) -> Vector:
    sum_vector = reduce(lambda point_1, point_2: point_1 + point_2, points)
    result_x = sum_vector.x / len(points)
    result_y = sum_vector.y / len(points)
    return Vector(result_x, result_y)


if __name__ == '__main__':
    first_vector = Vector(-1, -1)
    second_vector = Vector(2, 2)
    third_vector = Vector(3, 3)

    print(get_center_of_mass([first_vector, second_vector, third_vector]))
