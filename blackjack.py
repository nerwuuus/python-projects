import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
values = [("A",11), (2,2), (3,3), (4,4),(5,5), (6,6), (7,7), (8,8), (9,9), (10,10),("J",10), ("Q",10), ("K",10)]

ask_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

user_won = False
user_blackjack = False
computer_won = False
computer_blackjack = False

def computer_choice():
    global computer_cards, computer_score
    computer_cards = [random.choice(values)[1], random.choice(values)[1]]
    computer_score = sum(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}.")

def user_choice():
    global user_cards, user_score
    user_cards = [random.choice(values)[1], random.choice(values)[1]]
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}.")

def user_2nd_choice():
    global user_cards, user_score
    user_cards.append(random.choice(values)[1])
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")

def computer_2nd_choice():
    global computer_cards, computer_score
    while computer_score < 17:
        computer_cards.append(random.choice(values)[1])
        computer_score = sum(computer_cards)
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

def ace(user_score, computer_score):
    global user_cards, user_score
    if user_score > 21 and 11 in user_cards:
        i = user_cards.index(11) # find index of the first ace occurrence
        user_cards[i] = 1 # replace 11 with 1
        user_score = sum(user_cards)

    global computer_cards, computer_score
    if computer_score > 21 and 11 in computer_cards:
        x = computer_cards.index(11) # find index of the first ace occurrence
        computer_cards[x] = 1 # replace 11 with 1
        computer_score = sum(computer_cards)

def who_wins():
    global user_won, computer_won, computer_blackjack, user_blackjack
    if (11 in computer_cards and 10 in computer_cards) and (11 in user_cards and 10 in user_cards):
        computer_blackjack = False
        computer_won = False
        user_blackjack = False
        user_won = False
        print('Draw!')
    elif 11 in user_cards and 10 in user_cards:
        user_blackjack = True
        user_won = True
        print(f'Blackjack! You won! Your score is {user_score}. Computer chose {computer_cards}.')
    elif 11 in computer_cards and 10 in computer_cards:
        computer_blackjack = True
        computer_won = True
        user_blackjack = False
        user_won = False
        print(f'Blackjack! Computer wins! Computer chose {computer_cards}.')
    elif user_score > 21:
        print(f'Computer wins! Computer chose {computer_cards}. Your score is {user_score}.')
    elif user_score == 21:
        print(f'Blackjack! You won! Your score is {user_score}. Computer chose {computer_cards}.')

if ask_user == 'y':
    print(art.logo)

    user_choice()
    computer_choice()
    ace(user_score, computer_score)

    hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    another_choice = True
    if hit_or_stand == 'y':

        while another_choice:
            hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            user_2nd_choice()
            computer_2nd_choice()
            ace(user_score, computer_score)

            if user_score > 21:
                another_choice = False
                user_won = False
                computer_won = True

    who_wins()
