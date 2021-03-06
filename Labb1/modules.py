from random import randint


def remnant_numbers(number1, number2):
    total_number_list = []
    for i in range(1, 1000):
        if i % int(number1) == 0 and i % int(number2) == 0 and i:
            total_number_list.append(i)
    return total_number_list


def try_input():
    random_number = randint(1, 100)
    number_of_tries = 1
    while True:
        guess = input()
        if int(guess) == random_number:
            print(f"You were right! The answer was {random_number}, it took you {number_of_tries} try/tries.")
            break
        elif int(guess) < random_number:
            number_of_tries += 1
            print("Your guess was too low, try again.")
        elif int(guess) > random_number:
            number_of_tries += 1
            print("Your guess was too high, try again.")
