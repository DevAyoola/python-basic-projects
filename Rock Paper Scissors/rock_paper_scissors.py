# Rock Paper Scissors Game

import random

def play(rounds):
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    
    while(rounds>0):
        user_action = input("Enter a choice (rock, paper, scissors): ")
        print(f"You chose {user_action}, and computer chose {computer_action}")
            
        if user_action == computer_action:
            print(f"Both players chose {user_action}. It's a draw!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors. You won!")
            else:
                print("Paper covers rock. You lost!")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper. You won!")
            else:
                print("Rock smashes scissors. You lost!")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock. You won!")
            else:
                print("Scissors cuts paper. You lost!")

        rounds -= 1

if __name__ == "__main__":
    rounds = int(input("How many rounds? "))
    play(rounds)
    
