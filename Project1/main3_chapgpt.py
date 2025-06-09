'''
THIS IS IMPORT FROM CHATGPT
'''
import random

def get_computer_choice():
    return random.choice(["snake", "water", "gun"])

def get_user_choice():
    choice = input("Enter your choice (snake, water, gun): ").lower()
    while choice not in ["snake", "water", "gun"]:
        print("Invalid choice. Please choose again.")
        choice = input("Enter your choice (snake, water, gun): ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Snake, Water, Gun Game!")
    user_score = 0
    computer_score = 0
    rounds = int(input("How many rounds would you like to play? "))

    for round in range(1, rounds + 1):
        print(f"\nRound {round}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            print("You win this round!")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a draw.")

    print("\nFinal Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations, you won the game!")
    elif user_score < computer_score:
        print("😞 You lost. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
