class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Bike(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Car(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

car1 = Car("car", "hjdjn", "400cc")

print(car1.model)

