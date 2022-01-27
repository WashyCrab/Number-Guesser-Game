
# NUMBER GUESSING GAME


# Imports
from random import randrange


def main():

    while True:  # Lets the user input how many numbers there will be
        roof = input("Enter how many possible numbers you would like there to be. "
                     "Ex 10: ")
        while True:
            try:
                int(roof)
                break
            except ValueError:
                print("Please enter a whole number.")
        if int(roof) <= 0:
            print("Number must be greater than 0")
        else:
            break

    while True:  # Lets the user input how many guesses they will have
        guess_limit = input("Enter how many guesses you will have: ")

        while True:
            try:
                int(guess_limit)
                break
            except ValueError:
                print("Please enter a whole number: ")
        if int(guess_limit) <= 0:
            print("The guess limit must be greater than 0")
        else:
            break

    roof = int(roof)
    number = randrange(1, roof+1)
    g_count = 0

    guess_limit = int(guess_limit)

    while g_count < guess_limit:
        while True:
            guess = input(f"Enter your guess, (1-{roof}). You have {guess_limit - g_count}"
                          f" guesses left: ")

            try:
                int(guess)
                if 1 > int(guess) or int(guess) > roof:
                    print(f"Your guess of {guess} was outside of the possible numbers.")
                else:
                    break
            except ValueError:
                print("Please enter a whole number.")

        g_count += 1

        guess = int(guess)
        if guess == number:
            print(f"You win! The number was {number}. It took you {g_count} tries.")
            while True:
                play_again = input("Would you like to play again? (yes/no): ").lower()
                if play_again == 'yes':
                    main()
                if play_again == 'no':
                    print("Ok, bye!")
                    quit()
                else:
                    print("Please enter either yes or no.")

        if guess > number:
            print(f"The number is less than {guess}.")
        if guess < number:
            print(f"The number is greater than {guess}.")

    print(f"You ran out of guesses! The number was {number}")

    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again == 'yes':
            main()
        if play_again == 'no':
            print("Ok, bye!")
            quit()
        else:
            print("Please enter either yes or no.")


main()
