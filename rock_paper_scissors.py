import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# list of choices
images = [rock, paper, scissors]

# get user input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# get the image
if user_input >= 0 and user_input <= 2:
    print(images[user_input])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(images[computer_choice])

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You lose!")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input == 2:
    print("You win!")
elif computer_choice > user_input:
    print("You lose!")
elif user_input > computer_choice:
    print("You win!")
elif user_input == computer_choice:
    print("Draw.")
