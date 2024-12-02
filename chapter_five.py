from chapter_six import chapter_six

def chapter_five(character):
    """Chapter 5: Quest to the Ancient Ruins"""
    print("\n--- Chapter 5: Quest to the Ancient Ruins ---")
    print(f"Equipped with your {character['gear']}, you arrive at the entrance of the ancient ruins.")
    print("The ruins are shrouded in mystery, and the air is thick with magic.")
    print("As you proceed, magical creatures appear and block your path!")

    while True:
        print("\nWhat will you do?")
        print("1. Fight the magical creatures.")
        print("2. Run away.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            fight_creatures(character)
            break
        elif choice == "2":
            print("\nYou decide to run away, but as you exit the ruins, a group of elves surrounds you.")
            print("They accuse you of trespassing in their sacred lands and capture you.")
            chapter_six(character, captured=True)
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


def fight_creatures(character):
    """Handle the fight with magical creatures"""
    print("\n--- Fight with Magical Creatures ---")
    print("You must decide whether to use your new gear or your old equipment.")

    while True:
        print("\nWhat will you use?")
        print("1. Use your new gear.")
        print("2. Use your old equipment.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print(f"\nYou wield your {character['gear']} and face the magical creatures head-on.")
            print("With skill and strategy, you defeat the creatures and discover a powerful magic item!")
            character['magic_item'] = "Ancient Amulet of Power"
            print(f"You acquire the {character['magic_item']}!")
            print("However, as you leave the ruins, you are captured by a group of elves.")
            print("They accuse you of trespassing in their sacred lands.")
            chapter_six(character, captured=True)
            break
        elif choice == "2":
            print("\nYou rely on your old equipment, but it is no match for the magical creatures.")
            print("The creatures overwhelm you, and your journey ends here. Better luck next time!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
