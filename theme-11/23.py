class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



point1 = Point(2, 3)
point2 = Point(5, 7)

result = point1 + point2
# result = point1.__add__(point2)

# print(result.x, result.y)
print(point1 == point2)
print(point1 is point2)