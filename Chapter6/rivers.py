rivers = {
    'columbia river': 'united states',
    'elbe river': 'germany',
    'river thames': 'united kingdom'
}

print()
for river, nation in rivers.items():
    print(f'{river.title()} is in {nation.title()}')
print()
for river in rivers.keys():
    print(f'{river.title()}')
print()
for river, nation in rivers.items():
    print(f'{nation.title()}')
print()