"""Import important things."""
from random import choice
from hero import Hero


class Team:
    """Define Team class."""

    def __init__(self, name):
        """Initialize Team properties."""
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        """Remove hero from the heroes list."""
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
            else:
                return 0

    def view_all_heroes(self):
        """Loop through heroes and print out their names."""
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        """Add hero to the team."""
        self.heroes.append(hero)

    def stats(self):
        """Show stats for fight."""
        for hero in self.heroes:
            kd = hero.kills / hero.num_deaths
            print("{} Kill/Deaths: {}".format(hero.name, kd))

    def revive_heroes(self):
        """Revive dead hero."""
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        """Attack!"""
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            your_hero = choice(self.heroes)
            opponent_hero = choice(other_team.heroes)
            your_hero.fight(opponent_hero)
            if your_hero.fight(opponent_hero) == your_hero:
                living_opponents.remove(opponent_hero)
            else:
                living_heroes.remove(your_hero)
        return f'{your_hero.fight(opponent_hero)} is the winner!'
