import json
import os

#----------------------------------------------------------------------------------------------------------

def create_file(address, dictionary):
    if os.path.exists(address):
        os.remove(address)
    with open(address, 'w') as txt_obj:
        json.dump(definitions, txt_obj, indent = 4, sort_keys = True)
        print('File created!')
    txt_obj.close()

def load_file_info(address):
    with open(address) as txt_obj:
        info = json.load(txt_obj)
    print(info)
    txt_obj.close()

def file_append_new_info(address):
    moreEntries = True
    while moreEntries == True:
        key = input('Enter a new key: ')
        key = key.title()
        key = key.replace(' ', '')

        val = input('Enter a new value: ')
        val = val.title()
        val = val.replace(' ', '')

        entry = {
            key: val
        }

        with open(address, 'r+') as txt_obj:
            info = json.load(txt_obj)
            info.update(entry)
            txt_obj.seek(0)
            json.dump(info, txt_obj, indent = 4, sort_keys = True)
        txt_obj.close()

        msg = input('Would you like to continue adding new entries? Enter "y" if yes: ')
        if msg == 'y':
            moreEntries = True
        else:
            moreEntries = False

#----------------------------------------------------------------------------------------------------------

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
address = 'Chapter10/glossary.json'
menu_up = True

while menu_up == True:
    print('\n###\n')
    print('1) Create a new file')
    print('2) Print a previous file')
    print('3) Add to a previous file')
    print('4) Exit menu')
    print()
    num = input('Enter the number for your desired option: ')
    if num == '1':
        create_file(address, definitions)
    elif num == '2':
        load_file_info(address)
    elif num == '3':
        file_append_new_info(address)
    elif num == '4':
        menu_up = False
    else:
        print('Please only enter values 1 - 4.')
    print('\n###\n')