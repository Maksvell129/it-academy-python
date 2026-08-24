class Flyable:
    def fly(self):
        print("Летит")

class Swimmable:
    def swim(self):
        print("Плывёт")



class Duck(Flyable, Swimmable):
    pass



duck = Duck()

duck.fly()
duck.swim()
