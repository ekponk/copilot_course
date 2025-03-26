clues = [
    "There is a faint smell of smoke lingering in the air, as if a fire once raged here.",
    "There is a broken clock on the wall, its hands frozen at an ominous hour.",
    "There is a trail of muddy footprints leading deeper into the shadows.",
    "There is a torn piece of fabric caught on a jagged nail, fluttering slightly.",
    "There is a faint whisper echoing, though no one else seems to be around.",
    "There is a dusty book on the table, its pages filled with cryptic symbols.",
    "There is a shattered mirror on the floor, reflecting fragments of the room.",
    "There is a locked chest in the corner, its surface scratched as if someone tried to force it open.",
    "There is a flickering lightbulb overhead, casting eerie shadows on the walls.",
    "There is a strange chill in the air, as though something unseen is watching."
]

sense_exp = [
    "You see faint candlelight flickering in the distance, casting long shadows on the stone walls.",
    "You hear the distant echo of footsteps, though the corridor appears empty.",
    "You smell the damp, earthy scent of moss growing between the cracks in the stone floor.",
    "You feel a cold draft brushing against your skin, as if a hidden door has been left ajar.",
    "You sense an unshakable feeling of being watched, though no one is in sight.",
    "You see cobwebs draped across a forgotten chandelier, glinting faintly in the dim light.",
    "You hear the soft creak of wood, as if the castle itself is shifting in its slumber.",
    "You smell the faint aroma of burnt wood, as though a fire once roared in the nearby hearth.",
    "You feel the rough texture of the stone wall beneath your fingertips, worn smooth in places by time.",
    "You sense a strange warmth emanating from a nearby tapestry, as if it hides something alive.",
    "You see a faint trail of glowing dust leading toward a spiral staircase descending into darkness.",
    "You hear the faint murmur of voices, too quiet to understand, coming from behind a locked door."
]

import random

class RandomItemSelector:
    def __init__(self, items):
        """
        Initialize the RandomItemSelector with a list of items.
        :param items: List of items to select from.
        """
        self.items = items
        self.used_items = []

    def add_item(self, item):
        """
        Add a new item to the selection pool.
        :param item: The item to add.
        """
        self.items.append(item)

    def pull_random_item(self):
        """
        Select a random item from the list that hasn't been used yet.
        If all items have been used, reset the used items list.
        :return: A randomly selected item.
        """
        if len(self.used_items) == len(self.items):
            self.reset()
        
        available_items = [item for item in self.items if item not in self.used_items]
        selected_item = random.choice(available_items)
        self.used_items.append(selected_item)
        return selected_item

    def reset(self):
        """
        Reset the used items list, making all items available for selection again.
        """
        self.used_items = []

class SenseClueGenerator:
    _instance = None

    def __new__(cls):
        """
        Implement the singleton pattern to ensure only one instance of SenseClueGenerator exists.
        """
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            # Initialize RandomItemSelector instances for clues and sensory experiences
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        """
        Combine a random clue and sensory experience into a cohesive narrative.
        :return: A string combining a clue and a sensory experience.
        """
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"
    

from enum import Enum

class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2

from abc import ABC, abstractmethod

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self):
        """
        Run the encounter and return the outcome.
        :return: An EncounterOutcome indicating the result of the encounter.
        """
        pass


class DefaultEncounter(Encounter):
    def __init__(self):
        """
        Initialize the DefaultEncounter with an instance of SenseClueGenerator.
        """
        self.sense_clue_generator = SenseClueGenerator()

    def run_encounter(self):
        """
        Run the encounter by generating a random sense clue and printing it.
        :return: EncounterOutcome.CONTINUE
        """
        sense_clue = self.sense_clue_generator.get_senseclue()
        print(sense_clue)
        return EncounterOutcome.CONTINUE
    
class Room:
    def __init__(self, name, encounter):
        """
        Initialize the Room with a name and an encounter.
        :param name: The name of the room.
        :param encounter: An instance of an Encounter.
        """
        self.name = name
        self.encounter = encounter

    def visit_room(self):
        """
        Visit the room and run its encounter.
        :return: The result of the encounter's run_encounter method.
        """
        print(f"You have entered the {self.name}.")
        return self.encounter.run_encounter()
    

# Create a list of 6 room objects with unique names and default encounters
rooms = [
    Room("Grand Hall", DefaultEncounter()),
    Room("Dungeon", DefaultEncounter()),
    Room("Library of Shadows", DefaultEncounter()),
    Room("Armory", DefaultEncounter()),
    Room("Throne Room", DefaultEncounter()),
    Room("Tower Chamber", DefaultEncounter())
]


class Castle:
    def __init__(self):
        """
        Initialize the Castle with a RandomItemSelector for rooms.
        """
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        """
        Prompt the user to select a door from a random number of doors (2 to 4).
        :return: The selected door number.
        """
        import random
        num_doors = random.randint(2, 4)
        print(f"There are {num_doors} doors in front of you.")
        
        while True:
            try:
                selected_door = int(input(f"Select a door (1 to {num_doors}): "))
                if 1 <= selected_door <= num_doors:
                    return selected_door
                else:
                    print(f"Invalid choice. Please select a number between 1 and {num_doors}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def next_room(self):
        """
        Select a door, then choose a random room and visit it.
        :return: The result of the room's visit_room method.
        """
        selected_door = self.select_door()
        print(f"You selected door {selected_door}.")
        
        room = self.room_selector.pull_random_item()
        print(f"The door opens to reveal the {room.name}.")
        return room.visit_room()

    def reset(self):
        """
        Reset the room selector, making all rooms available again.
        """
        self.room_selector.reset()
        print("The castle has been reset. All rooms are now available again.")


class Game:
    def __init__(self, rooms):
        """
        Initialize the Game with a set of room objects.
        :param rooms: A set of Room objects.
        """
        self.castle = Castle()

    def play_game(self):
        """
        Start the game loop, allowing the player to navigate through the castle.
        """
        print("Welcome to the Castle Adventure!")
        print("Your objective is to navigate through the castle and find the treasure.")
        print("Good luck!")

        while True:
            outcome = self.castle.next_room()
            if outcome == EncounterOutcome.END:
                print("Game Over.")
                self.castle.reset()
                play_again = input("Would you like to explore a different castle? (yes/no): ").strip().lower()
                if play_again != "yes":
                    print("Thank you for playing! Goodbye!")
                    break
            elif outcome == EncounterOutcome.CONTINUE:
                print("You continue your journey through the castle.")


if __name__ == "__main__":
    # Start the game with the predefined rooms
    game = Game(rooms)
    game.play_game()