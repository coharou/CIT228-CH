print()
#
users = ['admin', 'coharou', 'haroutc', 'haroutu', 'charou']
if users:
    for e in users:
        if e == 'admin':
            print(f'{e.title()}, please reenter your passcode to proceed.')
        else:
            print(f'Welcome to the site, {e}!')
else:
    print('We need to find more users.')
#
print()