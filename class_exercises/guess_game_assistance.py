guess = int(input(" Guess a number: "))
lucky_number = 17
tries = 0

while tries < 3:
    if guess == lucky_number:
        print("Shey you dey whine me niiiiiiiiii, how you get am ")
        break

    else:

        if guess < lucky_number:
            print("Try again, the lucky number is higher ")
        tries += 1

        if guess > lucky_number:
            print("Try again, the lucky number is lesser ")

        guess = int(input(" Guess a number: "))

        if tries == 3:
            print("Werey no come here again you don fail tire ")

