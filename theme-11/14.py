class Engine:
    def start(self):
        print("Двигатель запущен")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
        # self.gear = Gear()


bmw_engine = Eengine()

car = Car(engine=bmw_engine)

car.engine.start()
