# jogos.py

import hangman
import divination


def choose_game():
    print("*********************************")
    print("******* Choose your game!*******")
    print("*********************************")

    print("(1) Hangman (2) Number Divination")

    game = int(input("Which game? "))

    if game == 1:
        print("Hang in there! You choose Hangman!")
        hangman.play()
    elif game == 2:
        print("Guess the secret number!")
        divination.play()


if __name__ == "__main__":
    choose_game()
