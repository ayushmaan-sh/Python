fruit = "banana"
color = "yellow"

if fruit != "banana":
    print("Does this fruit exist? Please check!")
    exit()

if fruit == "banana":
    if color == "green":
        print("Unripe, wait untill it gets fully ripe")
    elif color == "yellow":
        print("Ripe, you can eat it")
    elif color == "brown":
        print("It's unripe, you cannot eat this")