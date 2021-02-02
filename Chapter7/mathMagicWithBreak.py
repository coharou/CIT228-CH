import random
counter = 0
numIncorrect = 0
while counter < 10:
    randNum1 = random.randrange(1, 1000)
    randNum2 = random.randrange(1, 1000)
    correctAns = int(randNum1 + randNum2)
    userAns = int(input(f'What is the result of {randNum1} + {randNum2}?'))
    if userAns == correctAns:
        print('Your response was correct.')
    else:
        print(f'False. The correct answer is {correctAns}.')
        numIncorrect += 1
    counter += 1
    if numIncorrect > 5:
        print('You answered more than 5 problems incorrectly. It might be worthwhile to consider a tutor or practicing more.')
        break

