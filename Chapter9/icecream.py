from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'strawberry', 'mint', 'chocolate', 'pecan', 'pistachio']
    def DisplayIceCreamFlavor(self):
        for flavor in self.flavors:
            print(flavor.title())