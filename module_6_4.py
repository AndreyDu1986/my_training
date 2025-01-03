class Figure:
    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        if len(sides) != self.sides_count:
            sides = [1 for _ in range(self.sides_count)]
        self.__sides = sides

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, new_sides):
        return (
            len(new_sides) == self.sides_count
            and all(isinstance(side, int) and side > 0 for side in new_sides)
        )

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

import math

class Circle(Figure):
    @property
    def sides_count(self):
        return 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        circumference = self.get_sides()[0]
        return circumference / (2 * math.pi)

    def get_square(self):
        radius = self.__radius
        return math.pi * radius ** 2

def heron_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

class Triangle(Figure):
    @property
    def sides_count(self):
        return 3

    def get_square(self):
        a, b, c = self.get_sides()
        return heron_formula(a, b, c)

class Cube(Figure):
    @property
    def sides_count(self):
        return 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * 12

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(222, 35, 130)
print(cube1.get_color())
cube1.set_sides(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())