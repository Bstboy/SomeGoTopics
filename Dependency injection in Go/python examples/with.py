# Constructor Injection
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car started")

# Usage
engine = Engine()
car = Car(engine)
car.start()



# Method Injection
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def set_engine(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car started")

# Usage
engine1 = Engine()
car = Car()
car.set_engine(engine1)
car.start()

# Swapping out engine
engine2 = Engine()
car.set_engine(engine2)
car.start()
