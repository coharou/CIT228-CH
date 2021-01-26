animals = ['pig', 'cow', 'sheep', 'goat', 'horse', 'chicken']
animals2 = animals[0:]
animals2.append('buffalo')
animals2.append('deer')
animals2.append('turkey')
animals2.append('duck')

print()
print('/// First animals list')
for i in animals:
    print(i)
print()
print('/// Second animals list')
for i in animals2:
    print(i)
print()
print('/// Exercise 4.10')
print(f'The first three items in the list are: {animals2[0:3]}')
print(f'Three items from the middle of the list are: {animals2[4:7]}')
print(f'The last three items in the list are: {animals2[7:10]}')