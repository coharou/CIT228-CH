definitions = {
    'tuple': 'stores multiple values in one object',
    'slice': 'a division of an array that separates it into two parts, ideally for copying',
    'pop': 'removing an item from the end of an array',
    'elif': 'acts as a continuation between if and else in if-else statements',
    'float': 'values that contain numbers separated by decimals',
    'string': 'text based data type',
    'list': 'an object that stores multiple values, in which the values are assigned an index number for later reference',
    'dictionary': 'an object that stores key-value pairs',
    'integer': 'whole number data type',
    'constants': 'variables with a single, unchanging value'
}

for name, details in definitions.items():
    print(f'{name.title()}: {details}')