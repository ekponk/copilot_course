import random

# Define the rules of the game
RULES = {
    "scissors": ["lizard", "paper"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

OPTIONS = list(RULES.keys())


def get_user_choice():
    """Prompt the user to select an option."""
    #print("Options: rock, paper, scissors, lizard, spock")
    print("Options:")
    for i,(k,v) in enumerate(RULES.items()):
        print(f"{i+1} {k}")

    choice = input("Enter your choice (name or number): ").strip().lower()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(OPTIONS):
            choice = OPTIONS[index]
        else:
            choice = ""
    while choice not in OPTIONS:
        print("Invalid choice. Please choose again.")
        choice = input("Enter your choice: ").strip().lower()
    return choice  # Return the choice as a string

def get_computer_choice():
    """Randomly select an option for the computer."""
    return random.choice(OPTIONS)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules."""
    if user_choice == computer_choice:
        return "draw"
    elif computer_choice in RULES[user_choice]:
        return "user"
    else:
        return "computer"

def main():
    """Main function to run the game."""
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    if result == "draw":
        print("It's a draw!")
    elif result == "user":
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()