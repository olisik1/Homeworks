class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides if len(sides) == self.__class__.sides_count else [1] * self.__class__.sides_count
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.__class__.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)



import math

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.__calculate_radius()



class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5



class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = [sides[0]] * self.__class__.sides_count if len(sides) == 1 else self.get_sides()

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = [new_sides[0]] * self.__class__.sides_count
        else:
            super().set_sides(*new_sides)

    def get_volume(self):
        if len(self.__sides) >= 12:
            a = self.__sides[0]
            return a ** 3
        return None


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())  # Изменится

cube1.set_color(300, 70, 15)
print(cube1.get_color())  # Не изменится

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())  # Не изменится

circle1.set_sides(15)
print(circle1.get_sides())  # Изменится

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())