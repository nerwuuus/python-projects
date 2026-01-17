import random
from game_data import data
from art import logo
from art import vs

print(logo)
print("\n")

user_score = 0
a_follower_count = random.choice(data)['follower_count']
b_follower_count = random.choice(data)['follower_count']
game_over = False

# =================================================================
# DO POPRAWY, WYBIERA LOSOWE, NIEDOPASOWANE DO OSÓB ZAWODY I KRAJE
def choose_a():
    a_name = random.choice(data)['name']
    a_description = random.choice(data)['description']
    a_country = random.choice(data)['country']
    # a_follower_count = random.choice(data)['follower_count']
    print(f"Compare A: {a_name}, {a_description}, {a_country}.")

def choose_b():
    b_name = random.choice(data)['name']
    b_description = random.choice(data)['description']
    b_country = random.choice(data)['country']
    # b_follower_count = random.choice(data)['follower_count']
    print(f"Against B: {b_name}, {b_description}, {b_country}.")
# =================================================================

def choose():
    choose_a()
    print(vs)
    choose_b()

choose()
user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

if user_choice == 'a' and a_follower_count > b_follower_count:
    user_score += 1
    print(f"You're right! Current score: {user_score}")
    while not game_over:
        choose_a()
else:
    game_over = True
    print(f"You lost!")
