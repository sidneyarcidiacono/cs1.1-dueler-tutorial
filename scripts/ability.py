"""Import random library."""
import random


class Ability:
    """Define Ability class."""

    def __init__(self, name, max_damage):
        """Initialize ability properties."""
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """Attack values for ability."""
        random_value = random.randint(0, self.max_damage)
        return random_value


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
