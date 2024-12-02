from chapter_nine import chapter_nine

def chapter_eight(character):
    """Chapter 8: Back in the Capital"""
    print("\n--- Chapter 8: Back in the Capital ---")
    print("You return to the bustling capital, greeted by familiar sights and sounds.")
    print("At the adventurer's guild, you are approached by a guild master with an intriguing proposition.")
    print("'We've received reports of a powerful artifact hidden on a mysterious island,' the guild master says.")
    print("'This could be a once-in-a-lifetime opportunity, but it is dangerous. Are you up for the challenge?'")

    while True:
        print("\nWhat will you do?")
        print("1. Accept the quest.")
        print("2. Decline the quest.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\n--- Accepting the Quest ---")
            print("You agree to take on the quest, eager to uncover the secrets of the unknown islands.")
            print("The guild provides you with supplies and directions to a port where your journey will begin.")
            chapter_nine(character)
            break
        elif choice == "2":
            print("\n--- Declining the Quest ---")
            print("You decide to decline the quest, choosing a quieter life within the capital.")
            print("Perhaps one day, the allure of adventure will call to you again.")
            print("Your adventure ends here. Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
