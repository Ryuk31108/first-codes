import random

def game():
    attempts = 7
    pick = random.randint(1, 100)
    attempt = 0
    playing = True
    while playing == True:
        while attempt < attempts:
            guess = int(input("Enter Your Guess: "))
            attempt += 1
            if guess == pick:
                print("You WON!")
                return again()
            elif guess > pick:
                print("Number is lower")
                print("You have", attempt, "attempt(s) used")
            elif guess < pick:
                print("Number is higher")
                print("You have", attempt, "attempt(s) used")
            if attempt >= attempts:
                print("You lost. The number was", pick)
                return again()

def again():
    if input("Play again? (yes/no): ").strip().lower() == "yes":
            game()
            if input("Play again? (yes/no): ").strip().lower() == "no":
                    exit()

print("You have 7 attempts to guess a number from 1 to 100.")
while input("Type Start or Exit: ").strip().lower() == "start":
    game()
    if input("Type Start or Exit: ").strip().lower() == "exit":
        exit
