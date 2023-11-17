import random


def game(user, computer):
    # The user or computer have a blackjack
    if score(user) == 21:
        print(f"Your final hand {user}, final score {score(user)}")
        print(f"Computer's final hand {computer}, final score {score(computer)}")
        print("You win by Blackjack")

    elif computer == 21:
        print(f"Your final hand {user}, final score {score(user)}")
        print(f"Computer's final hand {computer}, final score {score(computer)}")
        print("You lose by Blackjack")

    # The user's score over 21 and have a "Ace"
    if 11 in user and score(computer) > 21:
        user[11] = 1

    elif score(user) == 21 and score(user) == score(computer):
        print(f"\tYour cards: {user}, current score: {score(user)}")
        print(f"Computer's final hand {computer}, final score {score(computer)}")
        print("Draw")


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

    game(user_cards, computer_cards)

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
    print(user_cards)
    print(computer_cards)