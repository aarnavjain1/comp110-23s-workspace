"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730384690"

secret_word: str = "python"
length_of_word: int = len(secret_word)
guess: str = input(f"What is your { length_of_word }-letter guess? ")
game: bool = True

while game:
    if guess == secret_word:
        print("Woo! You got it!")
        game = False
    if guess != secret_word and len(guess) == len(secret_word):
        print("Not quite. Play again soon! ")
        game = False
    if len(guess) != len(secret_word):
        guess = input(f"That was not { length_of_word } letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji_color: str = ""
guessed_character: bool = False
index_1: int = 0

while index<len(secret_word):
    if(guess[index]==secret_word[index]):
        emoji_color=emoji_color+GREEN_BOX
    else:
        while index_1<len(secret_word):
            if secret_word[index_1] == guess[index]:
                guessed_character = True
            index_1=index_1+1
        if guessed_character:
            emoji_color=emoji_color+YELLOW_BOX
        else:
            emoji_color=emoji_color+WHITE_BOX
    index=index+1
    guessed_character=False
    index_1=0
print(emoji_color)

