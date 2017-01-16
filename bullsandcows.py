#!/usr/bin/python
# encoding:utf-8
# BULLS & COWS game
# text-based guessing game, computer will generate number, player has to gues it
# right numbers in wrong positions are cows, right numbers in right positins
# are bulls


from random import randint

# generate random number with four distinct digits


def generate_number():
    a = str(randint(1, 9))
    number = [a]
    while True:
        x = len(number)
        n = str(randint(0, 9))
        if x == 4:
            break
        elif n not in number:
            number.append(n)
            continue
        else:
            continue
    return number

# user input validation


def valid_user_input(x):
    try:
        if len(x) == 4:
            return True
    except ValueError:
        return False

# evaluation of the game, according to no. of counts needed to guess the number


def evaluate(x):
    if x < 5:
        return("amazing!")
    elif x < 10:
        return("very good!")
    elif x < 15:
        return("not so bad...")
    else:
        return("not so good...")

# player guess and evaluation of the turn
# don't accept more than 4 digits and don't count it like a valid turn


def game():
    default = generate_number()
    turns_count = 0

    while True:
        guess = list(input("Guess the number (4 digit): "))
        bulls = 0
        cows = 0

        if not valid_user_input(guess):
            print("Four digits, please!")
            continue

        else:
            if guess == default:  # player guessed the number
                turns_count += 1
                result = evaluate(turns_count)
                print("Congratulation! You guessed the number in ",
                      turns_count, "turns. That is", result)
                break

            else:
                turns_count += 1

                for x in range(4):  # equal numbers in particular positions
                    if guess[x] == default[x]:
                        bulls += 1
                    else:
                        pass

                for digit in guess:  # looking for same numbers in both lists
                    if digit in default:
                        cows += 1
                    else:
                        pass

                cows_count = cows - bulls

                print(bulls, "bulls, " if bulls != 1 else "bull, ",
                      cows_count, "cows" if cows_count != 1 else "cow")


def main():
    while True:
        answer = str(
            input("Welcome to Bulls & Cows game, do you wanna play? Y/N "))

        if answer == "Y":
            print("Ok, I generated 4 digit number for you. Let's play:")
            game()

        else:
            print("OK. Maybe next time.")
            break

main()
