import random

# Choices available
choices = ['rock', 'paper', 'scissors']

# Score tracking
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!\n")
    elif winner == "user":
        print("You win this round!\n")
    else:
        print("Computer wins this round!\n")

def play_game():
    global user_score, computer_score

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        # Update score
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Show scores
        print(f"Score - You: {user_score} | Computer: {computer_score}\n")

        # Ask to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Score - You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("You are the overall winner!")
            elif computer_score > user_score:
                print("Computer is the overall winner!")
            else:
                print("It's an overall tie!")
            break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors Game!")
    play_game()
