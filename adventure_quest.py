# Import the random module to generate random numbers
import random

# Define a class Player to represent the player character
class Player:
    # Initialize the player with a name, health set to 100, and an empty inventory
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

# Define a class Monster to represent enemy creatures
class Monster:
    # Initialize a monster with a name, health, and attack stats
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

# Define a function to display the game introduction
def show_intro():
    print("Welcome to AdventureQuest!")
    print("Embark on a journey, battle monsters, and collect treasures.")

# Define a function to randomly select a location for the player to explore
def explore():
    locations = ["Forest", "Cave", "Castle"]
    return random.choice(locations)

# Define a function to simulate a battle between the player and a monster
def battle(player, monster):
    print(f"A wild {monster.name} appears!")

    # Continue the battle until either the player or the monster's health drops to zero
    while player.health > 0 and monster.health > 0:
        print(f"{player.name}'s Health: {player.health}")
        print(f"{monster.name}'s Health: {monster.health}")

        # Prompt the player to choose an action (Attack or Run)
        action = input("Do you want to [A]ttack or [R]un? ").upper()

        if action == "A":  # If the player chooses to attack
            # Generate random attack values for both the player and the monster
            player_attack = random.randint(1, 20)
            monster_attack = random.randint(1, 15)

            # Display the results of the player's attack
            print(f"You attack the {monster.name} for {player_attack} damage.")
            monster.health -= player_attack

            # Check if the monster's health is zero or below, declare victory
            if monster.health <= 0:
                print(f"You defeated the {monster.name}!")
                return True

            # Display the results of the monster's counterattack
            print(f"The {monster.name} attacks you for {monster_attack} damage.")
            player.health -= monster_attack
        elif action == "R":  # If the player chooses to run
            print("You run away from the battle.")
            return False
        else:  # If the player enters an invalid action
            print("Invalid action. Try again.")

    # Return False if the player's health drops to zero
    return False

# Define the main function to orchestrate the game
def main():
    show_intro()

    # Prompt the player to enter their character's name
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    while True:
        # Randomly select a location for the player to explore
        current_location = explore()
        print(f"You find yourself in a {current_location}.")

        # Create a monster based on the current location
        if current_location == "Forest":
            monster = Monster("Goblin", 20, 10)
        elif current_location == "Cave":
            monster = Monster("Dragon", 50, 20)
        elif current_location == "Castle":
            monster = Monster("Evil Knight", 30, 15)

        # Execute the battle function and check if the player won
        if battle(player, monster):
            print(f"You found a treasure in the {current_location}!")
            player.inventory.append(f"{current_location} Treasure")

        # Prompt the player to continue their adventure or exit the game
        play_again = input("Do you want to continue your adventure? (y/n): ").lower()
        if play_again != 'y':
            break

    print("Thanks for playing AdventureQuest!")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
