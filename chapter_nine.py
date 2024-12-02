from chapter_ten import chapter_ten

def chapter_nine(character):
    """Chapter 9: Journey Through the Jungle"""
    print("\n--- Chapter 9: The Journey to the Unknown Islands ---")
    print(f"You land on the mysterious island, equipped with your {character['gear']}.")
    print("Dense jungle surrounds you, and the air is humid and filled with the sounds of wildlife.")
    print("As you make your way through the jungle, you encounter a group of pirates searching for treasure.")

    while True:
        print("\nWhat will you do?")
        print("1. Ask the pirates for directions.")
        print("2. Fight the pirates.")
        print("3. Sneak around the pirates.")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            ask_pirates(character)
            break
        elif choice == "2":
            fight_pirates(character)
            break
        elif choice == "3":
            sneak_around(character)
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def ask_pirates(character):
    """Ask the pirates for directions."""
    print("\n--- Asking the Pirates for Directions ---")
    print("You approach the pirates cautiously and ask for directions to the artifact.")
    print("The pirates smirk and say, 'Information comes at a price. Got any coin?'")

    while True:
        print("\nDo you want to give them coin?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\n--- Giving the Pirates Coin ---")
            print("You hand over some coin, and the pirates point toward a ruin on a hill.")
            print("They warn you about the dangers ahead and go back to their search.")
            chapter_ten(character)
            break
        elif choice == "2":
            print("\n--- Refusing to Pay ---")
            print("The pirates become hostile and attack you!")
            fight_pirates(character, forced=True)
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


def fight_pirates(character, forced=False):
    """Fight the pirates."""
    print("\n--- Fighting the Pirates ---")
    if forced:
        print("You are forced into battle after refusing to pay the pirates.")
    else:
        print("You decide to fight the pirates.")

    while True:
        print("\nHow will you fight?")
        print("1. Fight to kill.")
        print("2. Fight non-lethally.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\n--- Lethal Victory ---")
            print("You defeat the pirates with lethal force.")
            print("With no one left to guide you, you wander through the jungle and reach a crossroad.")
            crossroad(character)
            break
        elif choice == "2":
            print("\n--- Non-Lethal Victory ---")
            print("You defeat the pirates without killing them.")
            print("Impressed by your mercy, one of the pirates points toward a ruin on a hill before retreating.")
            chapter_ten(character)
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


def sneak_around(character):
    """Sneak around the pirates."""
    print("\n--- Sneaking Around the Pirates ---")
    print("You decide to avoid confrontation and sneak around the pirates.")
    print("After some careful navigation, you find yourself back on the path, but the jungle grows denser.")
    print("Eventually, you reach a crossroad.")
    crossroad(character)


def crossroad(character):
    """Handle the jungle crossroad."""
    print("\n--- The Jungle Crossroad ---")
    print("You find yourself at a crossroad. One path leads left, and the other leads right.")
    print("The left path appears to ascend toward a hill, while the right path disappears into dense undergrowth.")

    while True:
        print("\nWhich path will you take?")
        print("1. Left")
        print("2. Right")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\n--- Left Path ---")
            print("You follow the left path and soon find yourself at the base of a ruin on the hill.")
            chapter_ten(character)
            break
        elif choice == "2":
            print("\n--- Right Path ---")
            print("You follow the right path but soon trigger a trap!")
            print("Vines and spikes trap you, and you barely manage to escape with your life.")
            print("Realizing your mistake, you retrace your steps and take the left path instead.")
            chapter_ten(character)
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
