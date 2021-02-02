mountains = {
    'Rocky Mountains': ['United States', 'canada'],
    'Himalayas': ['nepal', 'china'],
    'Alps': ['france', 'monaco', 'switzerland', 'germany', 'italy', 'austria', 'slovenia']
}

for mtn, c in mountains.items():
    print(f'{mtn}:')
    for i in c:
        print(f'-- {i.title()}')