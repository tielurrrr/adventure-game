from chapter_eight import chapter_eight

def chapter_seven(character):
    """Chapter 7: Defeating the Powerful Creature"""
    print("\n--- Chapter 7: Defeating the Powerful Creature ---")
    print("You and the elves venture deep into their sacred lands, where the powerful creature resides.")
    print("The air grows heavy with magic, and a chilling roar echoes as the creature appears.")
    print("The elves immediately engage in battle, their leader leading the charge.")

    print("\nAs the battle begins, the boss creature summons a horde of magical creatures to its side.")

    while True:
        print("\nWhat will you do?")
        print("1. Stay back and observe.")
        print("2. Join the elves and fight the summoned creatures.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            stay_back(character)
            break
        elif choice == "2":
            fight_with_elves(character)
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


def stay_back(character):
    """Stay back and let the elves handle the fight."""
    print("\n--- Staying Back ---")
    print("You decide to stay back and watch as the elves engage the summoned creatures.")
    print("The fight is brutal, and the majority of the elves are defeated.")
    print("Only the elf leader survives, barely standing. The summoned creatures are defeated, but the boss remains.")
    fight_boss(character, elf_leader_only=True)


def fight_with_elves(character):
    """Fight with the elves against the summoned creatures."""
    print("\n--- Fighting with the Elves ---")
    print("You join the elves in battling the summoned creatures.")
    print("Together, you manage to defeat the horde, but the boss creature remains.")
    print("The elf leader rallies you to face the boss together.")
    fight_boss(character, elf_leader_only=False)


def fight_boss(character, elf_leader_only):
    """Fight the boss creature with or without the support of the elves."""
    print("\n--- Boss Fight ---")
    if elf_leader_only:
        print("With the elf leader as the only remaining ally, you face the powerful boss creature.")
    else:
        print("With the elf leader and a few remaining elves, you prepare to fight the boss creature.")

    while True:
        print("\nWhat will you do?")
        print("1. Fight alongside the elf leader.")
        print("2. Let the elf leader be the decoy.")
        print("3. Run away.")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            print("\n--- Fighting Alongside the Elf Leader ---")
            print("You and the elf leader fight bravely against the boss.")
            print("With combined efforts, you defeat the creature!")
            if elf_leader_only:
                print("The elf leader thanks you for your bravery.")
            else:
                print("The elves celebrate the victory and thank you for your heroism.")
            reward_player(character)
            break
        elif choice == "2":
            print("\n--- Letting the Elf Leader Be the Decoy ---")
            print("You let the elf leader distract the boss while you deal the final blow.")
            print("The elf leader sacrifices themselves, but you manage to defeat the boss.")
            print("With a heavy heart, you leave the land of the elves, bearing the weight of their leader's death.")
            print("Your adventure continues, but the cost was great.")
            chapter_eight(character)
            break
        elif choice == "3":
            print("\n--- Running Away ---")
            print("You abandon the fight and flee. The elves are left to fend for themselves.")
            print("The boss creature remains undefeated, and your adventure ends in shame.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


def reward_player(character):
    """Reward the player for defeating the boss."""
    print("\n--- Victory and Reward ---")
    print("The elves reward you with a legendary piece of gear for your heroism.")
    character['gear'] = "Legendary Elven Armor"
    print(f"You receive the {character['gear']}!")
    print("With this new gear, your adventure takes a promising turn.")
    chapter_eight(character)
