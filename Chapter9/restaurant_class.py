class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'{self.restaurant_name}: a center for {self.cuisine_type} cuisine.')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!')

mcdonalds = Restaurant("McDonald's", 'American')
print(mcdonalds.restaurant_name)
print(mcdonalds.cuisine_type)
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()

bk = Restaurant("Burger King", 'American')
bk.describe_restaurant()

checkers = Restaurant("Checkers", 'American')
checkers.describe_restaurant()

rallys = Restaurant("Rally's", 'American')
rallys.describe_restaurant()