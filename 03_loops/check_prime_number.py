number = 10

is_prime = True  # aasuming that it's a prime number

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)