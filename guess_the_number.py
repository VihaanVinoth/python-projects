import random

num1 = random.randint(1, 100)
guesses = 0

print("I'm thinking of a number between 1 and 100.\nCan you guess what it is?\n")

while True:
    num = int(input("Guess the number: "))
    if 1 <= num <= 100:
        if num < num1:
            print("Too low!")
            guesses += 1
        elif num > num1:
            print("Too high!")
            guesses += 1
        elif num == num1:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break
    else:
        guesses += 1
        print("Invalid input. Please enter a number between 1 and 100.")
