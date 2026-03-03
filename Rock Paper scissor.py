import random

choices=['rock','paper','scissor']

def get_user_choice():
    while True:
        choice=input("Enter rock, paper or scissor ").lower()
        if choice in choices:
            return choice
        else:
            print("Incorrect choice, please try again")

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    
    if user==computer:
        return "tie"
    elif (user=='rock' and computer=="scissor") or (user=='paper' and computer=='rock') or (user=='scissor' and computer=='paper'):
        return "user"
    else:
        return "computer"


def play_game():

    user_score=0
    computer_score=0
    round_number=1

    while True:
        print(f"Rount Number {round_number}")

        user = get_user_choice()
        computer=get_computer_choice()
        print(f"Your choioce: {user}")
        print(f"computer choice {computer}")

        winner=decide_winner(user,computer)

        if winner == "tie":
            print("Result: It's a tie!")

        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1

        else:
            print("Result: Computer wins this round!")
            computer_score += 1
        
        print(f"Score --> You: {user_score} | Computer: {computer_score}")

        # Replay option
        play_again=input("Play another round? (yes/no): ").lower()
        if play_again!='yes':
            break
        
        round_number+=1
    
    print("\n=== Final Score ===")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    if user_score > computer_score:
        print("🎉 You are the overall winner!")
    elif computer_score > user_score:
        print("💻 Computer is the overall winner!")
    else:
        print("🤝 Overall match is a tie!")


# Run the game
play_game()