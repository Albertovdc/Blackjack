import random


def aces(cards):
    """The user's score over 21 and have a Ace """
    if 11 in cards and score(cards) > 21:
        cards[11] = 1
    return cards


def blackjack(cards):
    if score(cards) == 21:
        return True


def game(user, computer):
    """ Who win? """

    if score(user) == 21 and score(user) == score(computer):
        print(f"\tYour cards: {user}, current score: {score(user)}")
        print(f"Computer's final hand {computer}, final score {score(computer)}")
        print("You lose")

    elif score(user) > 21:
        print(f"\tYour cards: {user}, current score: {score(user)}")
        print(f"Computer's final hand {computer}, final score {score(computer)}")
        print("You lose")

    elif score(user) > score(computer) and score(user) < 21:
        print(f"\tYour cards: {user}, current score: {score(user)}")
        print(f"Computer's final hand {computer}, final score {score(computer)}")
        print("You win")



def computer_play(user, computer):
    elif score(computer) < 21 and score(computer) < score(user):
        computer += [card()]
        game(user, computer)

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

    user_cards = aces(user_cards)
    computer_cards = aces(computer_cards)

    # The user or computer have a blackjack?
    if blackjack(user_cards):
        print(f"Your final hand {user_cards}, final score {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("You win by Blackjack")
    elif blackjack(computer_cards):
        print(f"Your final hand {user_cards}, final score {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("You lose by Blackjack")

    blackjack = True
    # No? Then the game start.
    while blackjack:

        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's cards {computer_cards}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        chose = input("Type 'y' to get another card, type 'n' to pass: ")
        if chose == "y":
            # Create a function that returns
            if user_score < 21:
                user_cards += [card()]
                game(user_cards, computer_cards)
                user_score = score(user_cards)
                if user_score > 21:
                    blackjack = False
            # game(user_cards, computer_cards)
        elif chose == "n":
            if computer_score < 21 and computer_score < user_cards:
                computer_cards += [card()]
                game(user_cards, computer_cards)
                if computer_score > 21:
                    blackjack = False


            blackjack = False

    # print(user_cards)
    # print(computer_cards)
