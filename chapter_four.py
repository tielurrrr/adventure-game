from chapter_five import chapter_five

def chapter_four(character):
    """Chapter 4: Adventure in the Capital"""
    print("\n--- Chapter 4: Adventure in the Capital ---")
    print(f"{character['name']} arrives at the grand capital, a city of marvels and opportunities.")
    print("Your first stop is the bustling market to shop for gear.")
    go_shopping(character)

    print("\nAfter shopping, you head to the guild.")
    visit_guild(character)


def go_shopping(character):
    """Shopping for gear"""
    print("\n--- Shopping for Gear ---")
    print("You arrive at the market, where merchants display a variety of weapons and equipment.")
    print("You have the option to buy one of the following items:")
    print("1. New Staff (for magical power).")
    print("2. New Sword (for balanced combat).")
    print("3. New Dagger (for stealth and speed).")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            character['gear'] = "New Staff"
            print("\nYou purchase a gleaming staff, humming with magical energy.")
            break
        elif choice == "2":
            character['gear'] = "New Sword"
            print("\nYou purchase a finely crafted sword, sturdy and sharp.")
            break
        elif choice == "3":
            character['gear'] = "New Dagger"
            print("\nYou purchase a sleek dagger, perfect for quick strikes.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

    print(f"You are now equipped with a {character['gear']}.")


def visit_guild(character):
    """Visit the guild and decide whether to sign up"""
    print("\n--- Guild Visit ---")
    print("The guild is bustling with activity, filled with adventurers preparing for their next quests.")
    print("A receptionist greets you and offers you the chance to sign up as an adventurer.")

    while True:
        print("\nDo you want to sign up as an adventurer?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nYou sign up at the guild and officially become an adventurer!")
            print("The receptionist assigns you your first quest: Explore the ancient ruins outside the city.")
            print("You prepare yourself for the journey ahead.")
            chapter_five(character)
            break
        elif choice == "2":
            print("\nYou decide not to sign up, choosing a quieter life.")
            print("Your adventure ends here, but the capital remains a place of wonders.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
