print()
numbers = range(1, 10)
msg = ''
for i in numbers:
    msg += f'{str(i ** 3)}, '
print(msg)
cubes = [i ** 3 for i in numbers]
print(cubes)
print()