class Animal:
    def make_sound(self):
        print("Животное издаёт звук")


class Dog(Animal):
    def make_sound(self):
        print("Гав-гав")


class Cat(Animal):
    def make_sound(self):
        print("Мяу")


class Cow(Animal):
    def make_sound(self):
        print("Му-у")


animals = [
    Dog(),
    Cat(),
    Cow(),
]

for animal in animals:
    animal.make_sound()


