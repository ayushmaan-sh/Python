devs = {"ayush":"tech_and_business", "amrit": "business","rajeev": "tech"}
print(devs)

# get any particular value of an key.
print(devs.get("ayush"))

# changing items
devs["amrit"] = "Sales/Business"
print(devs)

# iteration over dictionaries
for role in devs:
    print(role, devs[role])

# two variables are also allowed in loop during iteration in dictionaries.
for key, values in devs.items():
    print(key, values)


if "amrit" in devs:
    print("Amrit is doing business")

#  Adding items in dictionariess
devs["neeraj"] = "full stack"
print(devs)