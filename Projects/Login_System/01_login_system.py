import time

# Define variables
username = "Ayushmaan24"
password = "@ayush#24"
wait_time = 1  # Initial wait time in seconds
max_retries = 5  # Maximum number of retry attempts

# Counter for login attempts
attempts = 0

# Main login loop
while attempts <= max_retries:
    user_input = input("Enter your password: ")

    if user_input == password:
        print("Welcome,", username)
        break  # Successful login, exit the loop

    else:
        print("Wrong password.", attempts + 1, "Attempts. You'll only get 5 attempts. Try again after", wait_time, "seconds")
        time.sleep(wait_time)  # Pause the program for the specified time
        wait_time *= 2  # Double the wait time for the next attempt
        attempts += 1  # Track and increment the attempt counter
