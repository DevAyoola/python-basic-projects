# Word Guessing Game

import random

name = input("What's your name? ")
print("Good luck! ", name)

words = ['computer', 'science', 'programming', 'python',
         'player', 'rainbow', 'software', 'website',
         'dev', 'game']

word = random.choice(words)
guesses = ''

print("Guess the characters: ")

# Number of turns
turns = 12

while turns > 0:
    failed = 0

    # compares the characters of word to guess
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win!")
        print("The word is", word)
        break

    print()
    guess = input("Guess a character: ")
    
    guesses += guess

    # checks input with character in word
    if guess not in word:
        turns -= 1
        
        print("Wrong!")
        print("You have", turns, "more guesses.")
        
        if turns == 0:
            print("You lose!")
