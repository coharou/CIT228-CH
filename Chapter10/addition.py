userContinue = True
while userContinue == True:
    num1 = input('Please enter your first number: ')
    num2 = input('Please enter your second number: ')
    try:
        number = int(num1) + int(num2)
        print(number)
    except ValueError:
        print('Please only enter number values, not text characters.')
    userRes = input('Would you like to continue? If so, enter "y" here: ')
    if userRes == 'y':
        userContinue = True
    else:
        userContinue = False