from random import randint
class Die:
    def __init__(self):
        self.sides = 6
    def update_sides(self, sides):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))

print()
print('----------------------------------------')
print('Six sided die: ')
sixSideDie = Die()
i = 0
while i < 10:
    sixSideDie.roll_die()
    i += 1
print('----------------------------------------')
print('Ten sided die: ')
tenSideDie = Die()
tenSideDie.update_sides(10)
i = 0
while i < 10:
    tenSideDie.roll_die()
    i += 1
print('----------------------------------------')
print('Twenty sided die: ')
twentySideDie = Die()
twentySideDie.update_sides(20)
i = 0
while i < 10:
    twentySideDie.roll_die()
    i += 1
print('----------------------------------------')
print()

