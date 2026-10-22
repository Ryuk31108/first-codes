import random

# play again
def play_game():
    playing = True
    while playing:
        options = ["rock", "paper", "scissors"]
        user = input("Enter your choice (rock, paper, scissors): ").lower()
        if user not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        computer = random.choice(options)
        print(f"Computer Chose: {computer}")
#win and lose conditions
        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
            print("You WIN!")
        else:
            print("You LOSE!")
#play again?
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            playing = False
            print("Thanks for playing!")
            exit()
        else:
            play_game()

play_game()
