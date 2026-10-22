import random

#words
words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming', 'computer', 'science', 'algorithm', 'function', 'english','developer','cpu','chatgpt','claude','grok']

#hangman himself
hangman = {
    5: '''
        +---------+
        O         |
                  |
                  |
                __|__''',
    4: '''
        +---------+
        O         |
        |         |
                  |
                __|__''',
    3: '''
        +---------+
        O         |
       /|         |
                  |
                __|__''',
    2: '''
        +---------+
        O         |
       /|\\        |
                  |
                __|__''',
    1: '''
        +---------+
        O         |
       /|\\        |
       /          |
                __|__''',
    0: '''
        +---------+
        O         |
       /|\\        |
       / \\        |
                __|__'''
}

#play again? function
def playagain():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            return game()
        elif choice == 'n':
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
#game function
def game():
    #game setting
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = set()
    attempts = 6
    #display
    display = [letter if letter in guessed_letters else '_' for letter in word]
    total_let = len(word)
    #win conditions
    while attempts > 0:
        print(display, total_let)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters or guess in wrong_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word: 
            guessed_letters.add(guess)
            display = [letter if letter in guessed_letters else '_' for letter in word]
            if '_' not in display or guess == word:
                print("Congratulations! You've guessed the word:", word)
                playagain()
                break
        elif guess not in word and guess not in wrong_guesses:
            wrong_guesses.add(guess)
            attempts -= 1
            print(hangman[attempts])
            print("You have attempted " + str(attempts) + " times")
            if '_' in display and attempts == 0:
                print("you lose")
                playagain()

game()
