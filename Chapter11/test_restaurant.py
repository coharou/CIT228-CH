from restaurant import Restaurant
import unittest

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        name = 'Burger King'
        cuisine = 'American'
        self.restaurant = Restaurant(name, cuisine)
    def test_set_serve(self):
        self.restaurant.set_number_served()
        self.assertEqual(self.restaurant.number_served, 10)
    def test_increment_serve(self):
        self.restaurant.increment_number_served(100)
        self.assertEqual(self.restaurant.number_served, 103)

if __name__ == '__main__':
    unittest.main() 