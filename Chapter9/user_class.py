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

print()
john = User('John', 'Marshall', 'jmarsh', 'rT9043ap', 'jmarsh#01')
john.describe_user()
john.greet_user()
print()
ben = User('Ben', 'Barley', 'bbarle', '43jh492a', 'bbarle#01')
ben.describe_user()
ben.greet_user()
print()
arthur = User('Arthur', 'Barton', 'abarto', '4985a0zl', 'abarto#02')
arthur.describe_user()
arthur.greet_user()
print()
adams = User('Adams', 'Hall', 'ahalld', 'ash4o5la', 'ahalld#04')
adams.increment_login_attempts()
adams.increment_login_attempts()
adams.increment_login_attempts()
print(f'Attempts: {adams.login_attempts}')
adams.reset_login_attempts()
print(f'Attempts: {adams.login_attempts}')