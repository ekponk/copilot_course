import random

# Define the rules of the game
RULES = {
    "rock": {"beats": "scissors", "loses_to": "paper"},
    "scissors": {"beats": "paper", "loses_to": "rock"},
    "paper": {"beats": "rock", "loses_to": "scissors"}
}

def get_user_choice():
    """Prompt the user to select rock, paper, or scissors."""
    choices = list(RULES.keys())
    print("Choose your option:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice.capitalize()}")
    while True:
        user_input = input("Enter the number or name of your choice: ").strip().lower()
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= len(choices):
                return choices[user_input - 1]
            else:
                print("Invalid choice. Please select a valid option.")
        elif user_input in choices:
            return user_input
        else:
            print("Invalid input. Please enter a valid number or name.")

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(list(RULES.keys()))

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif RULES[user_choice]["beats"] == computer_choice:
        return "You win!"
    else:
        return "You lose!"

def main():
    """Main function to run the game."""
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

if __name__ == "__main__":
    main()