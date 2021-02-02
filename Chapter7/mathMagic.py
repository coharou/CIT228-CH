import random
problems = int(input('Enter the number of math problems you would like: '))
counter = 0
numCorrect = 0
while counter < problems:
    randNum1 = random.randrange(1, 1000)
    randNum2 = random.randrange(1, 1000)
    correctAns = int(randNum1 + randNum2)
    userAns = int(input(f'What is the result of {randNum1} + {randNum2}?'))
    if userAns == correctAns:
        print('Your response was correct.')
        numCorrect += 1
    else:
        print(f'False. The correct answer is {correctAns}.')
    counter += 1
print(f'{numCorrect} response(s) were correct out of {problems} problem(s).')

