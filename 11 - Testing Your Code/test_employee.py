import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Tests for employee.py"""

    def setUp(self):
        """
        Create an employee for use in all rest cases
        """
        self.employee = Employee("Luke", "Eltiste", 100000)

    def test_give_default_raise(self):
        """Test the default give_raise function"""
        initial_annual_salary = self.employee.annual_salary
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, initial_annual_salary + 5000)

    def test_give_custom_raise(self):
        """Test the function give_raise with a custom value"""
        initial_annual_salary = self.employee.annual_salary
        self.employee.give_raise(14999)
        self.assertEqual(self.employee.annual_salary, initial_annual_salary + 14999)


if __name__ == "__main__":
    unittest.main()