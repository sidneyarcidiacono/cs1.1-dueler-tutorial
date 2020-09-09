"""Import needed modules."""
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from random import choice

class Arena:
    """Define class Arena."""

    def __init__(self):
        """Initialize properties for our Arena."""
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        """Return ability with values from user input."""
        name = input('What is the ability name? ')
        try:
            max_damage = int(input('What is the max damage? '))
        except ValueError:
            print("Please enter a number.")
            max_damage = int(input('What is the max damage? '))
        return Ability(name, max_damage)

    def create_weapon(self, drop_weapon=None):
        """Return weapon with values from user input."""
        if drop_weapon:
            possible_weapons = ["Bad Joke", "BO", "Party Crasher", "The DEA"]
            bonus_weapon = choice(possible_weapons)
            name = input(f"[1] Laser Beam\n[2] MGK\n[3] Guy Who Talks Too Much\n[4] Banana\n[5] {bonus_weapon}\n\nYour choice: ")
        else:
            name = input("[1] Laser Beam\n[2] MGK\n[3] Guy Who Talks Too Much\n[4] Banana\n\nYour Choice: ")
        try:
            max_damage = int(input('What is the max damage? '))
            if not max_damage % 2 == 0:
                max_damage -= 1
        except ValueError:
            print("Please enter a number.")
            max_damage = int(input('What is the max damage? '))
        return Weapon(name, max_damage)

    def create_armor(self):
        """Return armor with values from user input."""
        name = input('What is the armor name? ')
        try:
            max_block_strength = int(input('What is the max block strength? '))
        except ValueError:
            print("Please enter a number.")
            max_block_strength = int(input('What is the max block strength? '))
        return Armor(name, max_block_strength)

    def create_hero(self):
        """Return Hero with value from user input"""
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               hero.add_ability(self.create_ability())
           elif add_item == "2":
               hero.add_weapon(self.create_weapon())
           elif add_item == "3":
               hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        """Prompt the user to buid team one"""
        try:
            numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        except ValueError:
            print("Please enter a number.")
            numOfTeamMembers = int(input("How many members would you like on Team One?\n"))

        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        """Prompt the user to build team two"""
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """Battle team_one and team_two together."""
        winner = self.team_one.attack(self.team_two)
        drop_weapon = False
        for hero in self.team_one.heroes:
            if winner == hero.name:
                print("{:-^50}".format("Congratulations - You get a new weapon!"))
                drop_weapon =  True
                return drop_weapon
        for hero in self.team_two.heroes:
            if winner == hero.name:
                print("{:-^50}".format("Congratulations - You get a new weapon!"))
                drop_weapon = True
                return drop_weapon

    def kill_death_stats(self):
        """Calculate the average K/D for team one and two."""
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"{self.team_one.name} average K/D was: {str(team_kills/team_deaths)}")
        print(f"{self.team_two.name} average K/D was: {str(team_kills/team_deaths)}")

    def surviving_heroes(self):
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print(f"Survived from {self.team_one.name}: {hero.name}")
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(f"Survived from {self.team_two.name}: {hero.name}")

    def show_stats(self):
        """Print battle stats to terminal."""
        self.kill_death_stats()
        self.surviving_heroes()

    def edit_team(self, play_again):
        """Allow user to edit team after first playthrough."""
        if play_again.lower() == "y":
            edit_team = input("Would you like to edit your team first? Y or N: ")
            if edit_team.lower() == "y":
                pick_team = input("[1] Edit Team One\n[2] Edit Team Two\n ")
                if pick_team == "1":
                    self.build_team_one()
                elif pick_team == "2":
                    self.build_team_two()
                else:
                    print("Invalid response - please try again.")
                    pick_team = input("[1] Edit Team One\n[2] Edit Team Two\n ")



if __name__ == "__main__":
    game_is_running = True
    drop_weapon = None

    # Instantiate Game Arena
    arena = Arena()

    print("\n")
    print("{:=^50}".format("WELCOME TO THE GAME"))
    print("\n")

    #Build Teams
    print("\n")
    print("{:~^50}".format("Build Your Team"))
    print("\n")
    arena.build_team_one()
    arena.build_team_two()

    print("\n")
    print("{:~^50}".format("Get Ready...Battle!"))
    print("\n")

    while game_is_running:

        drop_weapon = arena.team_battle()

        print("\n")
        print("{:~^50}".format("Stats:"))
        print("\n")

        arena.show_stats()

        print("\n")
        print("{:-^50}".format("Can you handle another battle?"))

        play_again = input("Play Again? Y or N: ")
        arena.edit_team(play_again)
        arena.create_weapon(drop_weapon)

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
