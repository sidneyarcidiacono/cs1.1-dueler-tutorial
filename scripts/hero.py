"""Import important things"""
from random import choice
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    """Define hero class."""

    def __init__(self, name, starting_health=100):
        """Initialize hero properties."""
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        """Make hero fight other hero."""
        winner = ''
        if self.abilities or opponent.abilities:
            while self.is_alive() and opponent.is_alive():
                self.attack()
                opponent.defend()
                opponent.take_damage(self.attack())
                opponent.attack()
                self.defend()
                self.take_damage(opponent.attack())
                if not opponent.is_alive():
                    winner = self.name
                    self.add_kill_statistics(1)
                    opponent.set_deaths(1)
                    break
                elif not self.is_alive():
                    winner = opponent.name
                    self.set_deaths(1)
                    opponent.add_kill_statistics(1)
                    break
        else:
            print('Draw!')
        return winner



    def add_ability(self, ability):
        """set abilities for hero."""
        self.abilities.append(ability)

    def attack(self):
        """Loop through abilities to return
        total damage (int)."""
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        """set armor for hero."""
        self.armors.append(armor)

    def add_weapon(self, weapon):
        """Set weapon for hero."""
        self.abilities.append(weapon)

    def add_kill_statistics(self, num_kills):
        """Add kill statistics to gameplay."""
        self.kills += num_kills

    def set_deaths(self, num_deaths):
        """Setter for deaths."""
        self.deaths += num_deaths

    def defend(self):
        total_block_amount = 0
        for armor in self.armors:
            total_block_amount += armor.block()
        return total_block_amount

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()
        return self.current_health

    def is_alive(self):
        is_alive = True
        if self.current_health <= 0:
            is_alive = False
        else:
            is_alive = True
        return is_alive




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
