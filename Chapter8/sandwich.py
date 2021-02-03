def SandwichFunc(*items):
    print('Sandwich ingredients: ')
    for i in items:
        print(f'--{i}')
print()
SandwichFunc('peanut butter', 'jelly')
SandwichFunc('cheese slice')
SandwichFunc('bacon', 'lettuce', 'tomato')
print()