from character import create_character
from chapter_one import chapter_one

def main():
    # Welcome and character creation
    print("Welcome to the Text-Based Adventure Game!")
    print("You will embark on an epic journey. But first, let's create your character.\n")
    character = create_character()

    print(f"\nWelcome, {character['name']} the {character['race']} {character['class']}!")
    print("Prepare yourself for an adventure of a lifetime.\n")

    # Start the adventure
    chapter_one(character)

if __name__ == "__main__":
    main()
