from random import choice


class Hangman:
    def __init__(self) -> None:
        self.new_word()
        self.__wrong_guesses = 0
        self.__guesses = set()
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
        repr = self.text_art[self.__wrong_guesses]
        if self.__wrong_guesses < 6:
            repr += f"""\n\nWord -> {self.print_word()}
Guessed Letters -> {', '.join(sorted(self.__guesses))}"""
        return repr

    def new_word(self) -> None:
        with open("words.txt", "r") as f:
            words = f.read().split()
            self.word = choice(words)

    def print_word(self) -> str:
        return "".join(
            letter if letter in self.__guesses else "_" for letter in self.word
        )

    def main(self) -> tuple[bool, str]:
        while True:
            print(self)
            if self.__wrong_guesses == 6:
                return (False, self.word)
            elif "_" not in self.print_word():
                return (True, self.word)
            while True:
                guess = input("Guess a Letter: ")
                if not guess.isalpha():
                    print("Please Enter a letter. ")
                elif len(guess) > 1:
                    print("Please only enter a single character.")
                elif guess in self.__guesses:
                    print("Letter already guessed, try a different one.")
                else:
                    break
            if guess not in self.word:
                self.__wrong_guesses += 1
            self.__guesses.add(guess)


if __name__ == "__main__":
    hangman = Hangman()
    result = hangman.main()
    if result[0]:
        print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝""")
    else:
        print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝""")
    print(f"The word was {result[1]}")
