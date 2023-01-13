# def __init__(self, , )
# def check_card_length(card_length):
# print("******************************")


card = input("Kindly Enter your card details to verify: ")
print("Credit Card Number: " + card)


def check_card_length(card_check):
    if 13 <= len(card) <= 16:
        print("Credit card length: ", len(card))
    else:
        print("Credit card length: Invalid Card Length ")


check_card_length(card)


def check_card_type(card_type):
    if card[0] == "4":
        print("Credit Card Type: Visa Cards ")

    elif card[0] == "5":
        print("Credit Card Type: MasterCard")

    elif card[0] == "3" or card[0] == "7":
        print("Credit Card Type: American Express Cards")

    elif card[0] == "6":
        print("Credit Card Type: Discover Cards")

    else:
        print("Credit Card Type: Invalid Card Type")


check_card_type(card)


def add_even_number_step_2(add_single_digits):
    sum_of_even_number = 0

    for i in range(len(card) - 2, -1, -2):
        sum_digit = int(card[i]) * 2

        if sum_digit > 9:
            first_number = sum_digit // 10
            second_number = sum_digit % 10
            new_number = first_number + second_number
            sum_of_even_number += new_number
        else:
            sum_of_even_number += sum_digit

    print("sum of even numbers is: ", sum_of_even_number)


add_even_number_step_2(card)


def add_odd_number_step_3(add_odd_places):
    sum_of_odd_number = 0

    for x in range(len(card) - 1, -1, -2):
        sum_odd_digit = int(card[x])

        if sum_odd_digit < 9:
            sum_of_odd_number += sum_odd_digit
    print("sum of odd numbers on card is: ", sum_of_odd_number)


add_odd_number_step_3(card)


def sum_from_step2_and_3():
    sum_of_odd_number = 0
    step_4 = sum_of_odd_number
    print("The results from step 2 and step 3 are: ", step_4)

    if step_4 % 10 == 0:
        print("Credit Card Validity Status: Valid")
    else:
        print("Credit Card Validity Status: Invalid")


sum_from_step2_and_3(card)
# print([sum_digit])
# print(card)

# multiply_card_no = card[i] * 2
# print(multiply_card_no)
# first_number_2 = sum_odd_digit // 10
# second_number_2 = sum_odd_digit % 10
# new_number_2 = first_number_2 + second_number_2
# print(sum_odd_digit)
