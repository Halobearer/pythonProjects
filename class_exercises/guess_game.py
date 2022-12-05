import random

guess_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 0

while tries < 2:

    if guess == guess_number:
        print("You got it right ")
        break

    else:
        guess = int(input("Guess a number between 1 and 100: "))
    tries = tries + 1

    if tries == 2:
        print("Try again later, It's unfortunate you could not guess", guess_number)
