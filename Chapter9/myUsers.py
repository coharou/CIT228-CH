from user import User
from privileges import Privileges
from admin import Admin
john = Admin('John', 'Marshall', 'jmarsh', 'rT9043ap', 'jmarsh#01')
john.privileges.show_privileges()