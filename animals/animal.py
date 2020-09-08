class Animal:
    """Create class Animal."""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')


class Frog(Animal):
    """Create class Frog, inherits from Animal."""

    def jump(self):
        print(f'{self.name} is jumping')



dog = Animal('baby')
dog.eat()
dog.drink()

hopper = Frog('Hopper')
hopper.eat()
hopper.drink()
hopper.jump()
