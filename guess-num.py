import random

def guess():
    number = random.randint(1, 200)
    attempts = 0
    guessed = False
    n = input("May I ask you for your name?\n")
    print(f"{n}, we are going to play a game. I am thinking of a number between 1 and 200.\nGo ahead. Guess!")

    while not guessed:
        try:
            user_guess = int(input("Guess: "))
            attempts += 1

            if attempts == 6:
                print(f"Nope. The number I was thinking of was {number}")
                if input("Do you want to play again? (yes/no) ").strip().lower() == "yes":
                    guess()  
                else:
                    print("Thanks for playing!")
                break

            elif user_guess < number:
                print("The guess of the number that you have entered is too low\nTry Again!")

            elif user_guess > number:
                print("The guess of the number that you have entered is too high\nTry Again!")

            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                guessed = True
                if input("Do you want to play again? (yes/no) ").strip().lower() == "yes":
                    guess()  
                else:
                    print("Thanks for playing!")
                break

        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    guess()
