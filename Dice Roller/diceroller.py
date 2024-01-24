# Dice Roller

import random
import os

def num_die():
    while True:
        n = str(input("Number of dice (1 or 2): "))
        valid_responses = ('1', '2')

        try:
            if n not in valid_responses:
                return ValueError('1 or 2 only')
            else: 
                return n
        except ValueError as err:
            print(err)
        
def roll_dice():
    min_value = 1
    max_value = 6
    roll_again = 'y'

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
        os.system('cls' if os.name == 'nt' else clear)
        amount = num_die()

        if amount == '2':
            print("Dice are rolling...")
            dice_1 = random.randint(min_value, max_value)
            dice_2 = random.randint(min_value, max_value)

            print("The values are: ")
            print("Dice 1: ", dice_1)
            print("Dice 2: ", dice_2)

            roll_again = input("Roll Again? (y/n) ")

        elif amount == '1':
            print("Die is rolling...")
            dice_1 = random.randint(min_value, max_value)
            print("Die is: ", dice_1)
            roll_again = input("Roll Again? (y/n) ")

if __name__ == "__main__":
    roll_dice()
