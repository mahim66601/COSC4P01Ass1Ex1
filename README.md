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