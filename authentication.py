import json
class User:

    failed_attempts = 0
    
    def __init__(self):
        self.failed_attempts = 0

    def login(self, username:str, password:str) -> bool:
        """Login function to check if the username and password are correct

        Args:
            username (str): username
            password (str): password

        Returns:
            bool: True if the username and password are correct, False otherwise
        """
        print(f'login internal failed attempts: {self.failed_attempts}')
        if username == '' or password == '':
            print('Username and password cannot be empty')
            return False
        with open('data.json', mode='r') as file:
            data = json.load(file)
        for u, p in data.items():
            if self.failed_attempts < 3 and (username == u and password == p):
                self.failed_attempts = 0
                return True
            elif self.failed_attempts >= 3:
                print('Too many failed login attempts, please try again later')
                return False
            else:
                self.failed_attempts += 1
                return False

    def main(self):
        """Main function to run the login program, until the user logs in successfully or has failed three times to login
        """
        while (self.failed_attempts <= 3):
            print(f'Failed attempts: {self.failed_attempts}')
            username = input('Enter username: ')
            password = input('Enter password: ')
            if self.login(username, password):
                print('Login successful')
                return
            else:
                print('Login failed')
                
if __name__ == '__main__':
    loginClass = User()
    loginClass.main()