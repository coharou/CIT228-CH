print()

# Exercise 1
print('\tExercise 1')

foods = ['ramen', 'tacos', 'couscous', 'hummus', 'apricots', 'cereal']
print(foods)

numbers = [60, 66, 5, 10, 25, 45]
print(numbers)

movies = ['The Siege of Jadotville', 'The Godfather', 'Star Wars: The Empire Strikes Back']
print(movies)

newList = [foods[0], foods[3], numbers[1], numbers[2], movies[1], movies[2]]
print(newList)

print(foods[-1])
print(str(numbers[1]) + " " + str(numbers[3]) + " " + str(numbers[5]))

print(movies[0] + ", " + movies[1] + ", " + movies[2])
print(newList[0] + " " + str(newList[2]) + " " + newList[4])

print()

# Exercise 2
print('\tExercise 2')

movies.append('The Departed')
print(movies)

numbers.insert(3, 53)
print(numbers)

foods.insert(5, 'granola bars')
print(foods)

del foods[5]
print(foods)

numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)

print()

# Exercise 3
print('\tExercise 3')
movies.sort()
print(movies)

foods.sort()
print(foods)

print(sorted(numbers))
print(numbers)

movies.reverse()
print(movies)

print()