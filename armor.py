"""Import random library"""
import random


class Armor:
    """Define Armor class."""

    def __init__(self, name, max_block_strength):
        """Initialize armor properties."""
        self.name = name
        self.max_block_strength = max_block_strength

    def block(self):
        """Return random value to set block strength."""
        random_value = random.randint(0, self.max_block_strength)
        return random_value


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
