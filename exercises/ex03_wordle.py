""""EX03 - Structured Wordle."""

__author__ = "730384690"

def contains_char(word: str, single_char: str) -> bool:
    assert len(single_char) == 1
    index: int = 0
    while index < len(word):
        if word[index] == single_char:
            return True
        else:
            index = index + 1
        return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    index: int = 0
    emoji_string: str = ""
    while index < len(secret):
        if (guess[index] == secret[index]):
            emoji_string = emoji_string + GREEN_BOX
        else:
            if contains_char(secret, guess[index]):
                emoji_string = emoji_string + YELLOW_BOX
            else:
                emoji_string = emoji_string + WHITE_BOX
        index = index + 1
    return emoji_string

def input_guess(length: int) -> str:
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} char! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
secret_word: str = "codes"
turns: int = 0
game_flow: bool = True
while game_flow and turns < 7:
    guess: str = input_guess(5)
    print(emojified(guess, secret_word))
    if secret_word == guess:
        print(f"You won in {turns}/6 turns!")
        game_flow = False
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")
        game_flow == False
    turns = turns + 1

if __name__ == "__main__":
    main()
