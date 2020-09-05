"""Import ability to inherit from, random library."""
from ability import Ability
import random

class Weapon(Ability):
    """Define weapon class, inherits from Ability."""

    def attack(self):
        """Override attack method from Ability."""
        random_value = random.randint(self.max_damage/2, self.max_damage)
        return random_value
