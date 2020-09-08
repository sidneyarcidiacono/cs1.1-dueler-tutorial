class Dog:
    """Create class Dog."""

    def __init__(self, name, breed):
        """Initialize dog properties."""
        self.name = name
        self.breed = breed
        print('Dog initialized!')

    def bark(self):
        """Make dog bark."""
        print('Woof!')

    def sit(self):
        """Make dog sit."""
        print('Doggie sits.')

    def roll_over(self):
        """Make dog roll over."""
        print('Doggie rolls over.')
