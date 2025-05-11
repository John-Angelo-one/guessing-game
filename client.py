import random
import socket

host = "localhost"
port = 7777

def auto(low, high):
    return str((low + high) // 2)

def get_range(difficulty):
    if difficulty == 1:
        return 1, 10
    elif difficulty == 2:
        return 1, 50
    elif difficulty == 3:
        return 1, 100
    else:
        return 1, 1000

def start_game():
    print("Welcome to the Guessing Game!")
    difficulty = int(input("Choose difficulty (1 = Easy, 2 = Medium, 3 = Hard): "))
    low, high = get_range(difficulty)

    number_to_guess = random.randint(low, high)
    attempts = 0
    guessed = False

    print(f"Guess a number between {low} and {high}.")

    while not guessed:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    start_game()
