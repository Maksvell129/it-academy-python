from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int



point1 = Point(1, 2)

print(type(point1))
print(point1.x, point1.y)
