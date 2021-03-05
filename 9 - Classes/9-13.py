import random


class Die:
    """A class to represent Dice"""

    def __init__(self, sides=6):
        """Constructor"""
        self.sides = sides

    def roll_die(self):
        print(f"The die rolled {random.randint(1, self.sides)}")


d6 = Die()
d10 = Die(10)
d20 = Die(20)

print("Rolling 6 sided die:")
for i in range(10):
    d6.roll_die()

print("Rolling 10 sided die:")
for i in range(10):
    d10.roll_die()

print("Rolling 20 sided die:")
for i in range(10):
    d20.roll_die()