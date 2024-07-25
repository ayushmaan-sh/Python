Laptops = ("Asus", "Lenevo", "Macbook", "Dell")
print(Laptops)

# As tuples are immutable, value can't be change. We can change the references, but not the existing tuple.
# Example: Laptops[0] = "Acer"  -> we cannot do this in tuple
# Rest all of the things we can do what we were doing with lists.

# Adding tuples
more_laptops = ("chuwi", "Acer")
all_laptops = more_laptops + Laptops
print(all_laptops)

# counting any specific value in tuple
count = all_laptops.count("chuwi")
print(count)

# making variables in tuples
(asus, lenevo, macbook, dell) = Laptops   # It is necessary that the number of values inside tuple should be equal to number of variables
print(asus)

# nested tuples -> ((), (), ())