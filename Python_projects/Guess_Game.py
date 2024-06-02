import random

def guessing_game():
    magic_number = random.randint(0, 100)
    attempts = 0
    
    print("Guess a magic number between 0 and 100")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < magic_number:
            print("Your guess is too low")
        elif guess > magic_number:
            print("Your guess is too high")
        else:
            print(f"Yes, the number is {magic_number}")
            print(f"Your total number of guesses is: {attempts}")
            break

if __name__ == "__main__":
    guessing_game()
