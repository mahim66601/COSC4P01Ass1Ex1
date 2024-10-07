import json

def login(username:str, password:str) -> bool:
    """Login function to check if the username and password are correct

    Args:
        username (str): username
        password (str): password

    Returns:
        bool: True if the username and password are correct, False otherwise
    """    
    if username == '' or password == '':
        print('Username and password cannot be empty')
        return False
    with open('data.json', mode='r') as file:
        data = json.load(file)
    for u, p in data.items():
        global failed_attempts # global variable to keep track of failed login attempts
        if failed_attempts < 3 and (username == u and password == p):
            failed_attempts = 0
            return True
        elif failed_attempts >= 3:
            print('Too many failed login attempts, please try again later')
            return False
        else:
            failed_attempts += 1
            return False

def main():
    """Main function to run the login program, until the user logs in successfully or has failed three times to login
    """
    global failed_attempts
    failed_attempts = 0
    while (failed_attempts <= 3):
        username = input('Enter username: ')
        password = input('Enter password: ')
        if login(username, password):
            print('Login successful')
        else:
            print('Login failed')

if __name__ == '__main__':
    main()
else:
    global failed_attempts
    failed_attempts = 0