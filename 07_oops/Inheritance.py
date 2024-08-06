# Create an electric Car class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Class Electric_Car inherits all the values of class Car
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_tesla = Electric_Car("Tesla", "Model S", "85KWh")
print(my_tesla.full_name())

myCar = Car("MG", "Hector")
print(myCar.full_name())

my_new_car = Car("Tesla", "Model X")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())
