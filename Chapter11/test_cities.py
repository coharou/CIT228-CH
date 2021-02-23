from city_functions import Get_Location
import unittest

class TestLocation(unittest.TestCase):
    def test_city_country(self):
        test_location = Get_Location('Traverse City', 'United States')
        self.assertEqual(test_location, 'Traverse City, United States')
    def test_city_country_population(self):
        test_location_pop = Get_Location('Traverse City', 'United States', '15500')
        self.assertEqual(test_location_pop, 'Traverse City, United States - population 15500')

if __name__ == '__main__':
    unittest.main() 