print('\n###\n')
'''
print('10-3: Guest')
guest = input('Please enter your name. ')
with open('Chapter10/guest.txt', 'w') as txt_obj:
    txt_obj.write(guest)
txt_obj.close()

print('\n###\n')

print('10-4: Guest Book')
with open('Chapter10/guest_book.txt', 'w') as txt_obj:
    moreGuests = True
    while moreGuests == True:
        new_guest = input('Please add a guest: ')
        txt_obj.write(f'{new_guest}\n')
        testUser = input('Would you like to continue? Enter "y" if so.')
        if testUser == 'y':
            moreGuests = True
        else:
            moreGuests = False
txt_obj.close()
'''
import os
import random
if os.path.exists('Chapter10/test.txt'):
    os.remove('Chapter10/test.txt')
with open('Chapter10/test.txt', 'w') as txt_obj:
    room_list = []
    moreGuests = True
    room_good = False
    while moreGuests == True:
        new_guest = input('Please add a guest: ')
        while room_good == False:
            room = random.randint(1, 50)
            if room in room_list:
                room_good = False
            else:
                room_list.append(room)
                room_good = True
        print(f'Your room number is {room}.')
        txt_obj.write(f'Guest: {new_guest} -- Room: {room}\n')
        testUser = input('Would you like to continue? Enter "y" if so.')
        if testUser == 'y':
            moreGuests = True
        else:
            moreGuests = False
txt_obj.close()
with open('Chapter10/test.txt') as txt_obj:
    print(txt_obj.read())
txt_obj.close()
print('\n###\n')