class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 3
    def describe_restaurant(self):
        print(f'{self.restaurant_name}: a center for {self.cuisine_type} cuisine.')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open!')
    def set_number_served(self):
        self.number_served = 10
    def increment_number_served(self, addserve):
        self.addserve = addserve
        self.number_served += self.addserve