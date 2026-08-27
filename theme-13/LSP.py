class Bird:
    def fly(self):
        print("Птица летит")


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError

class Soloway(Bird):
    pass


class Bird:
    pass


class Penguin(Bird):
    pass


class Flyable:
    def fly(self):
        print("Летим")


class Soloway(Bird, Flyable):
    pass


