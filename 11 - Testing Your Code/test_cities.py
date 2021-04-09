import unittest
from city_functions import cityToString


class CityFunctionsTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_cities(self):
        """Does Santiago and Chile return the correct string"""
        formatted_city = cityToString("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

    def test_city_country_population(self):
        """Does Santiago and Chile with population return the correct string"""
        formatted_city = cityToString("Santiago", "Chile", population=5000000)
        self.assertEqual(formatted_city, "Santiago, Chile – population 5000000")


if __name__ == "__main__":
    unittest.main()