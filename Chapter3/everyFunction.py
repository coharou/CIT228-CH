print()
#

worldWonders = ['Hanging Gardens', 'Hagia Sophia', 'Eiffel Tower', 'Statue of Liberty', 'CN Tower']
print(f'Main:\t\t{worldWonders}')

worldWonders.append('Pyramids')
print(f'Append:\t\t{worldWonders}')

worldWonders.insert(0, 'Alhambra')
print(f'Insert:\t\t{worldWonders}')

del worldWonders[3]
print(f'Delete:\t\t{worldWonders}')

worldWonders.pop(2)
print(f'Pop:\t\t{worldWonders}')

worldWonders.remove('Alhambra')
print(f'Remove:\t\t{worldWonders}')

print(f'Sorted:\t\t{sorted(worldWonders)}')

worldWonders.sort()
print(f'Sort:\t\t{worldWonders}')

worldWonders.reverse()
print(f'Reverse:\t{worldWonders}')

print(f'Length:\t\t{len(worldWonders)}')

#
print()