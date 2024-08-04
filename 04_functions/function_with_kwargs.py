# Create a function that accepts any number of keywords arguments and prints them in the format key: value

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Tony Stark", power="Brain",enemy="Thanos")