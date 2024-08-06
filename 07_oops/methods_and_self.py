# Like in other langauges, there's is 'this' keyword. Python has 'self' keyword

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

myCar = Car("MG", "Hector")
print(myCar.full_name())

my_new_car = Car("Tesla", "Model X")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())
