from chapter_seven import chapter_seven

def chapter_six(character, captured=False):
    """Chapter 6: Captured by Elves"""
    print("\n--- Chapter 6: Captured by Elves ---")
    if captured:
        print("The elves escort you to their hidden village, where their leader awaits.")
        print("They are wary of your presence and suspect you may be a threat to their sacred lands.")
        print("The elven leader begins to interrogate you.")

        if 'magic_item' in character:
            handle_magic_item(character)
        else:
            handle_interrogation(character)
    else:
        print("You proceed deeper into the adventure. (Expand further with new challenges.)")


def handle_magic_item(character):
    """Handle the scenario where the player has the magic item."""
    print("\n--- Magic Item Detected ---")
    print(f"The elves notice the {character['magic_item']} in your possession.")
    print("The leader's expression softens as they recognize the artifact.")
    print("'You possess something of great significance,' the leader says.")
    print("'This proves you are not an enemy. We have need of someone like you.'")
    print("The elves release you and offer you an alliance.")
    print("You are asked to help them defeat a powerful creature threatening their land.")
    chapter_seven(character)


def handle_interrogation(character):
    """Handle the interrogation if the player has no magic item."""
    print("\n--- Interrogation ---")
    print("The leader begins a thorough interrogation.")
    print("'Who are you, and why are you trespassing in our sacred lands?'")

    truthful_answers = 0

    # First question
    while True:
        print("\nThe leader asks: 'Who are you?'")
        print("1. Tell the truth.")
        print("2. Lie.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nYou truthfully explain your name and your background.")
            truthful_answers += 1
            break
        elif choice == "2":
            print("\nYou provide a false identity, but the elves seem skeptical.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

    # Second question
    while True:
        print("\nThe leader asks: 'What are you doing in our lands?'")
        print("1. Tell the truth.")
        print("2. Lie.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("\nYou truthfully explain your quest and how you ended up in their territory.")
            truthful_answers += 1
            break
        elif choice == "2":
            print("\nYou fabricate a story, but the elves remain suspicious.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

    # Determine outcome
    if truthful_answers >= 1:
        print("\nThe leader nods slowly. 'You have spoken truthfully at least once,' they say.")
        print("'We will trust you, but only tentatively. We need your help with a grave matter.'")
        chapter_seven(character)
    else:
        print("\nThe leader frowns deeply. 'You have lied to us repeatedly,' they say.")
        print("The elves cannot trust you. Your journey ends here, as you are exiled from their lands.")
        print("Game Over.")
