import random


def play():
    print("*********************************")
    print("Welcome to Divination! Try to guess the secret number!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    points = 1000

    print("Levels:")
    print("(1) Easy (2) Mid (3) Hard")

    level = int(input("Choose the game level: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    for rounds in range(1, total_attempts + 1):
        print("Attempt {} of {}".format(rounds, total_attempts))

        guess_str = input("Enter a number between 1 and 100: ")
        print("You typed: ", guess_str)
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("You must enter a number between 1 and 100!")
            continue

        got_it_right = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if got_it_right:
            print("You got it right and scored {} points!".format(points))
            break
        else:
            lost_points = abs(secret_number - guess)
            points = points - lost_points
            if bigger:
                print("Your guessing was bigger than the secret number")
                if rounds == total_attempts:
                    print("The secret number was {}. You did {} points.".format(secret_number, points))
            elif smaller:
                print("You got it wrong! Your guess was less than the secret number.")
                if rounds == total_attempts:
                    print("The secret number was {}. You did {} points.".format(secret_number, points))

    print("End of the game!")


if __name__ == "__main__":
    play()
