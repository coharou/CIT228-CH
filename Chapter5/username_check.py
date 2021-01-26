print()
#

current_users = ['coharou', 'haroutc', 'haroutu', 'charou', 'charout']
current_users_lower = current_users[0:]

i = 0
for e in current_users_lower:
    e.lower()
    current_users_lower[i]
    i = i + 1

new_users = ['coharou', 'charou', 'colhar', 'colinh', 'colinharou']

for e in new_users:
    if e in current_users_lower:
        print(f'The name you have entered, {e}, has already been taken. Please reenter a new name.')
    else:
        print('The username you entered is ready for use.')

#
print()