"""
Castle Escape Game 
"""

# ---------- 1. SETUP: data the game needs ----------

# A tuple: the room names never change, so a tuple fits
ROOMS = ("Library", "Kitchen", "Dungeon", "Throne Room")

# The player only gets 4 turns in total
MAX_TURNS = 4

# A list: this changes as the player collects things
inventory = []

# What each room contains (room name -> item you can find there)
ROOM_ITEMS = {
    "Library": "access code",
    "Kitchen": "nothing useful",
    "Dungeon": "key",
    "Throne Room": "nothing useful",
}


# ---------- 2. FUNCTIONS: one job each ----------

def show_rooms(turns_left):
    """Print the list of rooms the player can choose from."""
    print(f"\nTurns left: {turns_left}")
    print("Which room do you enter?")
    for number, room in enumerate(ROOMS, start=1):
        print(f"  {number}. {room}")
    print("  5. Try to escape")


def explore_room(room):
    """Handle what happens when the player enters a room."""
    print(f"\nYou enter the {room}...")
    item = ROOM_ITEMS[room]

    if item == "nothing useful":
        print("You search everywhere but find nothing useful.")
    elif item in inventory:
        print(f"You already took the {item} from here.")
    else:
        print(f"You found the {item}!")
        inventory.append(item)


def try_escape():
    """Return True if the player has everything needed to escape."""
    if "key" in inventory and "access code" in inventory:
        print("\nYou unlock the door and enter the code. You escaped the castle!")
        return True
    else:
        print("\nThe door won't open. You're missing something.")
        return False


# ---------- 3. MAIN: ties everything together ----------

def main():
    print("=== CASTLE ESCAPE ===")
    print(f"You are trapped in a castle. You only have {MAX_TURNS} turns!")

    turns_left = MAX_TURNS
    escaped = False

    # Keep going while the player still has turns AND hasn't escaped
    while turns_left > 0 and not escaped:
        show_rooms(turns_left)
        choice = input("Enter a number: ")

        if choice in ("1", "2", "3", "4"):
            room = ROOMS[int(choice) - 1]
            explore_room(room)
            turns_left -= 1          # entering a room uses a turn
        elif choice == "5":
            escaped = try_escape()
            turns_left -= 1          # trying to escape also uses a turn
        else:
            print("Please enter a number from 1 to 5.")   # no turn lost for a typo

    # After the loop ends, check WHY it ended
    if not escaped:
        print("\nYou're out of turns! The castle guards found you. Game over.")
    print("Thanks for playing!")


# ---------- 4. START THE GAME ----------

# This line makes the game run only when you run this file directly
if __name__ == "__main__":
    main()
