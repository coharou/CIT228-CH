sandwich_orders = ['pastrami', 'peanut butter and jelly', 'pastrami', 'tuna', 'BLT', 'chicken', 'pastrami']
finished_sandwiches = []

print()

msg = ''
for s in sandwich_orders:
    msg += s + ' - '
print(f'Sandwich orders: {msg}')

print('The pastrami has ran out.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


for s in sandwich_orders:
    print(f'A {s} sandwich was made.')
    finished_sandwiches.append(s)

msg = ''
for s in finished_sandwiches:
    msg += s + ' - '
print(f'Finished sandwiches: {msg}')

print()