# Write a function that greets user with it's name. If no user input, greet a default name.

def greet(name = "User"):  #defined a default value
    return "Hello, "+name+"!"

print(greet())