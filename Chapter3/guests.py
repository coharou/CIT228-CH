print()
#

guests = ['Bill', 'George', 'Otto']
for e in guests:
    print(f'{e}, please come to my dinner party!')

print()
print('Otto is unable to come to the party.')
guests[2] = 'Will'
for e in guests:
    print(f'{e}, you are still invited to the party!')

print()
print('More tables were found for the party! Sending out more invites.')
guests.insert(0, 'Theo')
guests.insert(2, 'Ramsey')
guests.append('Ben')
for e in guests:
   print(f'{e}, please come to the reorganized party!')
print()
print(f'{len(guests)} people will be attending the party now.')

print()
print('Most of the tables were lost due to an error. Only 2 guests will be able to attend.')
i = 0
while i < 4:
    uninvited_guest = guests.pop()
    print(f'Sorry, {uninvited_guest}, but you will not be able to attend the party.')
    i = i + 1
print(f'{guests[0]} and {guests[1]} - you can still attend.')

del guests[0]
del guests[0]
print(guests)

#
print()