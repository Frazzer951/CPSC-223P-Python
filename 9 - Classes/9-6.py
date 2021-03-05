class Restaurant:
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Constructor for restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print out a statement describing the restaurant"""
        print(f"The restaurant {self.restaurant_name} has {self.cuisine_type} food")

    def open_restaurant(self):
        """Print out a statement saying the restaurant is open"""
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, num):
        """Set the number served"""
        self.number_served = num

    def increment_number_served(self):
        """Increment the number served"""
        self.number_served += 1


class IceCreamStand(Restaurant):
    """A Class to represent an Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Constructor"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Print out the flavors"""
        print(f"The ice cream stand has these flavors: {str(self.flavors).strip('[]')}")


icecream = IceCreamStand(
    "Luke's Ice", "Ice Cream", ["Chocolate", "Vanilla", "Mint Chip"]
)

icecream.display_flavors()