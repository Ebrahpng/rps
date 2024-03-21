import random

def get_choices():
    player_choice = input("enter a choice (rock, paper, scissors): ")
    
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors! you win!"
        else:
            return "paper covers rock! you lose."
        
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cut paper! you lose."
        
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper! you win!"
        else:
            return "rock smashes scissors! you lose."
        
choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)       
        
    