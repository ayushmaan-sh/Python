# Login System with Exponential Backoff

This Python code implements a login system with a retry mechanism using exponential backoff. It limits the number of login attempts and increases the waiting time between each failed attempt to prevent account lockout or system overload.

## Key Features

- **Practical Application of Exponential Backoff**: This project demonstrates how to handle login attempts using exponential backoff, a common strategy to manage retries in networked applications.
  
- **Improved User Experience**: By allowing multiple tries while preventing system abuse, the user experience is significantly enhanced. Users are given several opportunities to enter the correct credentials without risking account lockout.
  
- **Exponential Backoff Strategy**: The use of `time.sleep()` and a `wait_time` variable implements the exponential backoff strategy, increasing the delay between each failed login attempt to reduce server load and potential abuse.
  
- **Well-Structured Code**: The code is organized and includes informative print statements to provide feedback to the user, ensuring clarity and ease of understanding.

## How It Works

1. **User Input**: The system prompts the user to enter their login credentials.
2. **Authentication**: The system checks the provided credentials.
3. **Retry Mechanism**: If the credentials are incorrect, the system implements exponential backoff:
   - The wait time doubles after each failed attempt.
   - The user is informed about the wait time before the next attempt.
4. **Limit Attempts**: The system limits the number of login attempts to a predefined maximum to prevent abuse and potential security risks.

## Usage

1. Clone the repository.
2. Ensure you have Python installed on your machine.
3. Run the script using `python login_system.py`.
4. Follow the on-screen instructions to test the login system.

This project is a great example of how to handle user authentication attempts gracefully and securely. It can be expanded or integrated into larger applications where user authentication is required.

---

Feel free to explore the code and modify it according to your needs. Contributions and feedback are welcome!

