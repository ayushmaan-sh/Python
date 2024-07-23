chai_types = ["Black", "Green", "Oolong", "White"]

print(chai_types)

# Get an element from the list
print(chai_types[2])

# slicing elements from the list

# the last element of the slicing index (that is 3 in this example) is not included
print(chai_types[0:3])
# we can also mention only the starting or ending point
print(chai_types[:2])
print(chai_types[1:])

# chainging/replacing the element values

chai_types[3] = "Herbal"
print(chai_types)

# slicing dicing is tricky

# chai_types[2:3] = "Lemon" - Each alphabets of Lemon will become an array/list element.
# print(chai_types)
chai_types[2:3] = ["Lemon"] # Correct way, now the 'Lemon' only will become an element.
print(chai_types)
# we can also replace 2 elements like this
chai_types[1:3] = ["masala","Oolong"]
print(chai_types)

# playing with empty lists

print(chai_types[1:1]) # this will give an empty array

chai_types[1:1] = ["test1", "test2"]
print(chai_types)

chai_types[1:3] = [] # assinging an empty array will remove the elements. It can also be called delete operation.
print(chai_types)

# how to remove the last element from the list
chai_types.pop()
print(chai_types)

# how to remove any element from the list
chai_types.remove("Black")
print(chai_types)

# how to insert any element from the list
chai_types.insert(0, "Black")
print(chai_types)

# List Comprehentions - calculations inside list
num = [x**2 ]