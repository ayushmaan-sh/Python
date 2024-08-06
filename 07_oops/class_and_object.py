# Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Object
myCar = Car("MG", "Hector")

# We can make multiple object
myCar2 = Car("Tesla", "Model X")

print(myCar.brand)
