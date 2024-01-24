# Number guessing game

import math
import random

lower = int(input('Enter the lower bound: '))
upper = int(input('Enter the upper bound: '))

guess = random.randrange(lower, upper)
attempt = math.floor((upper - lower)/2)

while attempt >= 0:
    unum = int(input('Enter your guess: '))
    
    if attempt > 0:
        if unum == guess:
            print('Congratulations, You Got It!')
            break

        elif unum > upper or unum < lower:
            print('Sorry, Your guess is out of range!')
            break
        
        elif unum < guess:
            print('You guessed too small!')

        elif unum > guess:
            print('You guessed too high!')
        
    elif attempt == 0:
        print('Better Luck Next Time!')
        break
    
    attempt -= 1
