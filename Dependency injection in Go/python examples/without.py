"""
How can a class be independent from the creation of the objects it depends on?
How can an application, and the objects it uses support different configurations?
How can the behavior of a piece of code be changed without editing it directly?
"""

# without Depandancy Injection

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car started")

# Usage
car = Car()
car.start()
