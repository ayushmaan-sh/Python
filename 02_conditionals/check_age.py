# question -> classify the person's age groups: Child(<13), Teenager (13-19), Adult (20-59), Senior(60+)

# solution

age = 65

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
elif age < 60:
    print("You're a adult")
else:
    print("You're a senior")
