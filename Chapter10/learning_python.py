path = 'Chapter10/learning_python.txt'

print('\n###\n')
print('Part 1: .read()')
with open(path) as txt_obj:
    print(txt_obj.read())
txt_obj.close()

print('\n###\n')
print('Part 2: for loop')
with open(path) as txt_obj:
    for line in txt_obj:
        print(line)
txt_obj.close()

print('\n###\n')
print('Part 3: .readlines()')
with open(path) as txt_obj:
    txt_list = txt_obj.readlines()
    for line in txt_list:
        print(line)
txt_obj.close()

print('\n###\n')
print('Part 4: .replace()')
with open(path) as txt_obj:
    for line in txt_obj:
        new_line = line.replace('Python', 'Javascript')
        print(new_line)
txt_obj.close()

print('\n###\n')