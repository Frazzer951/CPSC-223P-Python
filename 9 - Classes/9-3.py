class User:
    """A basic user class"""

    def __init__(self, first_name, last_name, username, description):
        """Constructor for user class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.description = description

    def describe_user(self):
        """Print out a statement describing the user"""
        print(
            f"{self.first_name} {self.last_name} goes by the username {self.username}, and describes them self as so: {self.description}"
        )

    def greet_user(self):
        """Greet the user"""
        print(f"Welcome {self.first_name} {self.last_name} ({self.username})")


luke = User("Luke", "Eltiste", "Frazzer", "Programmer")
carl = User("Carl", "Hansson", "Snifs", "Media Consumer")
ryan = User("Ryan", "Daily", "Bonmonk", '"Gamer"')

luke.describe_user()
carl.describe_user()
ryan.describe_user()

luke.greet_user()
carl.greet_user()
ryan.greet_user()