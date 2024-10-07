# COSC4P01 Assignment 1 Exercise 1

The objective of the exercise is to develop a user login system using Python, following Test Driven Development (TDD) methodology. I will use Python 3.9.13 for the implementation, and pytest for the unit tests.

## Unit Test Cases

1. Verify that the username and password fields are not empty.
2. Verify that user login is successful when the username and password are correct.
3. Check that the username and password fields are case sensitive.
4. Verify user lockout on three failed login attempts.

## Test Results

Test No. | Description | Test Data | Expected Result | Actual Result | Status
--- | --- | --- | --- | --- | ---
1 | Verify that the username and password fields are not empty. | `username: "", password: ""` | `False` | `False` | Pass
2 | Verify that user login is successful when the username and password are correct. | `username: "admin", password: "admin"` | `True` | `True` | Pass
3 | Check that the username and password fields are case sensitive. | `username: "ADmin", password: "adMin"` | `False` | `False` | Pass
4 | Verify user lockout on three failed login attempts. | `username: "admin", password: "test"` entered three times, then `username: "admin", password: "admin"` | `False` | `False` | Pass

## Refactoring

- Encapsulated the login and main functions in the User class. This allows for code resuability and scalability.

- Renamed the login.py file to authentication.py to better reflect the purpose of the file.

- Replaced using a global failed_attempts counter with a class variable and an instance variable. Allows for multiple instances of the User class to have their own failed_attempts counter.

## Analysis

Following TDD principles gave me a clear direction on what to implement, and also helped me eliminate some trial and error when writing the code by forcing me to think of the test cases first. Handling the edge case where the username and password fields are empty when implementing the login method may not have been considered if I did not write the test cases first.
Implementing the required functionality while ensuring that the test cases pass also saved me time in debugging, as I could identify the issues early on and fix them before moving on to the next test case. It also helped me focus on the core functionality of the program and take a step-by-step approach to building the login system.