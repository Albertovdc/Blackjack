import random


def game(user, computer):
    if score(user) == 21:
        print(f"User {user}")
        print(f"Computer {computer}")
        print("You win Blackjack")
    elif score(user) > 21:
        print(f"User {user}")
        print(f"Computer {computer}")
        print("You lose")
    elif score(user) == score(computer):
        print(f"User {user}")
        print(f"Computer {computer}")
        print("Draw")
    elif score(computer) == 21:
        print(f"User {user}")
        print(f"Computer {computer}")
        print("You lose Blackjack")
    elif score(computer) <= 17 and score(computer) < 21:
        computer += [card()]
        game(user, computer)
    elif score(computer) < 21:
        computer += [card()]
        game(user, computer)
    elif score(computer) > 21:
        print(f"User {user}")
        print(f"Computer {computer}")
        print("You win")



def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    x = random.choice(cards)
    return x


def score(c):
    total = 0
    for item in c:
        total += item
    return total


chose = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if chose == "y":

    # Add random cards to computer and user
    user_cards = [card(), card()]
    computer_cards = [card(), card()]

    # Scores
    user_score = score(user_cards)
    computer_score = score(computer_cards)
    if 11 in user_cards and user_score > 21:
        user_cards[11] = 1

    elif user_score == 21:
        print(f"Your final hand {user_score}, final score {computer_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("You win by Blackjack")

    elif user_score == 21 and user_score == computer_score:
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("Draw")

    elif computer_score == 21:
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("You lose")

    while user_score < 21:

        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's cards {computer_cards}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        chose = input("Type 'y' to get another card, type 'n' to pass: ")
        if chose == "y":
            user_cards += [card()]
            game(user_cards, computer_cards)
            user_score = score(user_cards)
        if chose == "n":
            computer_cards += [card()]
            game(user_cards, computer_cards)
            computer_score = score(computer_cards)
            user_score = 30
