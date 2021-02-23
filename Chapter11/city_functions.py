def Get_Location(city, country, population = ''):
    location = f'{city}, {country}'
    if population != '':
        location += f' - population {population}'
    return location
