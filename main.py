import random


class Hangman:
    def __init__(self) -> None:
        self.new_word()
        self.__wrong_guesses = 0
        self.text_art = [
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
        ]

    def __repr__(self) -> str:
        return self.text_art[self.__wrong_guesses]

    def new_word(self) -> None:
        with open("words.txt", "r") as f:
            words = f.read().split()
            self.word = random.choice(words)


if __name__ == "__main__":
    hangman = Hangman()
    for i in range(7):
        hangman._Hangman__wrong_guesses = i
        print(hangman)
