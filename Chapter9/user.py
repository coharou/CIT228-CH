class User:
    def __init__(self, first_name, last_name, username, password, uid):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.uid = uid
        self.login_attempts = 0
    def describe_user(self):
        print(f'{self.last_name}, {self.first_name}')
        print(f'Username: {self.username}')
        print(f'UID: {self.uid}')
    def greet_user(self):
        print(f'Welcome, {self.first_name} {self.last_name} ({self.username})!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0