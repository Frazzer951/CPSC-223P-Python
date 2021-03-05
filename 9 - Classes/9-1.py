class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructor for restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print out a statement describing the restaurant"""
        print(f"The restaurant {self.restaurant_name} has {self.cuisine_type} food")

    def open_restaurant(self):
        """Print out a statement saying the restaurant is open"""
        print(f"{self.restaurant_name} is open")


mcdonald = Restaurant("McDonalds", "American")

mcdonald.describe_restaurant()
mcdonald.open_restaurant()