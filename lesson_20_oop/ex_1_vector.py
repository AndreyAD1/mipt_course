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


if __name__ == '__main__':
    first_vector = Vector(1, 1)
    second_vector = Vector(2, 5)
    print(first_vector + second_vector)
    print(first_vector - second_vector)
    print(first_vector * second_vector)
    print(-first_vector)
