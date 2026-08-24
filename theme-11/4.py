class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.area = width * height

    @property
    def area(self):
        return self.width * self.height

rectangle = Rectangle(10, 5)

print(rectangle.area)

rectangle.height = 10

print(rectangle.area)