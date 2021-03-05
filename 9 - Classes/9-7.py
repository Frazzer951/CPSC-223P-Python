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


class Admin(User):
    """A More Powerful User"""

    def __init__(self, first_name, last_name, username, description):
        """Constructor"""
        super().__init__(first_name, last_name, username, description)
        self.permissions = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print out the privileges an admin has"""
        print(f"The admin privileges include: {str(self.permissions).strip('[]')}")


luke = Admin("Luke", "Eltiste", "Frazzer", "Programmer")
luke.show_privileges()