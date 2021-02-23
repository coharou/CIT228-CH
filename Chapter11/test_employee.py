from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        first_name = 'First'
        last_name = 'Last'
        salary = 1
        self.employee = Employee(first_name, last_name, salary)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 5001)
    def test_give_custom_raise(self):
        self.employee.give_raise(200)
        self.assertEqual(self.employee.salary, 201)

if __name__ == '__main__':
    unittest.main() 