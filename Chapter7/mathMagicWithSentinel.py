import random

numCorrect = 0
userContinue = True

while userContinue:
    randNum1 = random.randrange(1, 1000)
    randNum2 = random.randrange(1, 1000)
    correctAns = int(randNum1 + randNum2)

    userAns = int(input(f'What is the result of {randNum1} + {randNum2}?'))
    if userAns == correctAns:
        print('Your response was correct.')
        numCorrect += 1
    else:
        print(f'False. The correct answer is {correctAns}.')

    userRes = input('Would you like to exit? Press "y" if so.')
    if userRes == 'y':
        userContinue = False

print(f'{numCorrect} response(s) were correct.')

