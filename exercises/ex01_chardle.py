"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730384690"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character_guess: str = input("Enter a single character: ")
if len(single_character_guess) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + single_character_guess + " in " + five_character_word)
number_of_instances: int = 0
    
if (single_character_guess == five_character_word[0]):
    number_of_instances = number_of_instances + 1
    print(single_character_guess + " found at index 0")
if (single_character_guess == five_character_word[1]):
    number_of_instances = number_of_instances + 1
    print(single_character_guess + " found at index 1")
if (single_character_guess == five_character_word[2]):
    number_of_instances = number_of_instances + 1
    print(single_character_guess + " found at index 2")
if (single_character_guess == five_character_word[3]):
    number_of_instances = number_of_instances + 1
    print(single_character_guess + " found at index 3")
if (single_character_guess == five_character_word[4]):
    number_of_instances = number_of_instances + 1
    print(single_character_guess + " found at index 4")

if number_of_instances == 0:
    print("No instances of " + single_character_guess + " found in " + five_character_word)
else:
    if number_of_instances == 1:
        print("1 instance of " + single_character_guess + " found in " + five_character_word)
    else:
        if number_of_instances == 2:
            print("2 instances of " + single_character_guess + " found in " + five_character_word)
        else:
            if number_of_instances == 3:
                print("3 instances of " + single_character_guess + " found in " + five_character_word)
            else:
                if number_of_instances == 4:
                    print("4 instances of " + single_character_guess + " found in " + five_character_word)
                else:
                    if number_of_instances == 5:
                        print("5 instances of " + single_character_guess + " found in " + five_character_word)
