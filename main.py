# This is a sample Python script.
import random
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def ask_for_name():
    input_name = input("Please enter your name: ")
    return input_name

def create_a_number(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('This is a game where you guess a number between 1 and 100')
    random_number = random.randint(1, 100)
    return random_number

def guess_the_number(number):

    while True:
        try:
            guess = input("Please enter your guess: ")
            guess = int(guess)
        except ValueError:
            print("Please enter a number")
            guess_the_number(number)
            continue
        print(number)
        if guess == number:
            print("You guessed the number!")
            return guess
        else :
            print("You did not guess the number ...")
            if guess > number:
                print("The number is lower.")

            elif guess < number:
                print("The number is higher.")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = create_a_number(ask_for_name())
    guess_the_number(number)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
