class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


# Square inherits Rectangle Class
class Square(Rectangle):
    # Square only requiring one argument
    def __init__(self, length):
        super().__init__(length, length)


# Prism inherits Rectangle Class
class Prism(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def get_volume(self):
        return super().get_area() * self.height

    def get_base_area(self):
        return super().get_area()

    def get_side_area_l(self):
        return self.length * self.height

    def get_side_area_w(self):
        return self.width * self.height

    def get_area(self):
        return 2 * (
            self.get_base_area() + 
            self.get_side_area_l() + 
            self.get_side_area_w()
        )


# RECTANGLE TEST
rectangle = Rectangle(1, 2)
other_rectangle = Rectangle(3, 4)
other_other_rectangle = Rectangle(1, 2)
print(f"Rectangle 1 area: {rectangle.get_area()}")
print(f"Rectangle 2 area: {other_rectangle.get_area()}")
print(f"Rectangle 3 area: {other_other_rectangle.get_area()}")

print(f"Rectangle 1 greater than Rectangle 2: {rectangle.__gt__(other_rectangle)}")
print(f"Rectangle 1 less than Rectangle 2: {rectangle.__lt__(other_rectangle)}")
print(f"Rectangle 1 equal to Rectangle 2: {rectangle.__eq__(other_rectangle)}")
print(f"Rectangle 1 equal to Rectangle 2: {rectangle.__eq__(other_other_rectangle)}")

# PRISM TESTS
prism = Prism(1, 2, 3)
other_prism = Prism(4, 5, 6)
print(f"Prism base area: {prism.get_base_area()}")
print(f"Prism area: {prism.get_area()}")
print(f"Prism volume: {prism.get_volume()}")

# SQUARE TESTS
square = Square(2)
print(f"Rectangle 1 area: {rectangle.get_area()}")
