class User:
    """A basic user class"""

    def __init__(self, first_name, last_name, username, description):
        """Constructor for user class"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.description = description
        self.login_attempts = 0

    def describe_user(self):
        """Print out a statement describing the user"""
        print(
            f"{self.first_name} {self.last_name} goes by the username {self.username}, and describes them self as so: {self.description}"
        )

    def greet_user(self):
        """Greet the user"""
        print(f"Welcome {self.first_name} {self.last_name} ({self.username})")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


luke = User("Luke", "Eltiste", "Frazzer", "Programmer")
luke.increment_login_attempts()
luke.increment_login_attempts()
luke.increment_login_attempts()
luke.increment_login_attempts()
print("Login attempts:", luke.login_attempts)
luke.reset_login_attempts()
print("Login attempts:", luke.login_attempts)
