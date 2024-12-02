def create_character():
    print("Character Creation:")
    name = input("Enter your character's name: ")
    race = input("Choose your race (Human, Elf, Dwarf, etc.): ")
    char_class = input("Choose your class (Warrior, Mage, Thief, etc.): ")

    character = {
        "name": name,
        "race": race,
        "class": char_class
    }
    print("\nCharacter created successfully!")
    return character
