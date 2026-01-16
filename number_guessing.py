import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Your role is to guess this number!")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.randint(1, 100)

def easy():
    attempts_easy = 10

    while attempts_easy != 0:
        print(f"You have {attempts_easy} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess != number:
            attempts_easy -= 1
            if guess > number:
                print('Too high!')
            else:
                print('Too low!')
    if guess != number:
        print(f"You've run out of attempts. The number was {number}.")

def hard():
    attempts_hard = 5

    while attempts_hard != 0:
        print(f"You have {attempts_hard} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess != number:
            attempts_hard -= 1
            if guess > number:
                print('Too high!')
            else:
                print('Too low!')
    if guess != number:
        print(f"You've run out of attempts. The number was {number}.")

if level == "easy":
    easy()
else:
    hard()
