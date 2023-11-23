import random


def ace(cards):
    """The user's score over 21 and have a Ace """
    if 11 in cards and score(cards) > 21:
        cards[11] = 1
    return cards


def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    n = random.choice(cards)
    return n


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

    user_cards = ace(user_cards)
    computer_cards = ace(computer_cards)

    # The user or computer have a blackjack?
    if user_score == 21:
        print(f"Your final hand {user_cards}, final score {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("You win by Blackjack")
    elif computer_score == 21:
        print(f"Your final hand {user_cards}, final score {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print("You lose by Blackjack")
    else:
        game = True
        while game:
            user_score = score(user_cards)
            print(f"\tYour cards: {user_cards}, current score: {user_score}")
            print(f"Computer's cards {computer_cards}")
            print(f"\tComputer's first card: {computer_cards[0]}")

            chose = input("Type 'y' to get another card, type 'n' to pass: ")
            if chose == "y":
                if user_score < 21:
                    user_cards += [card()]
                    user_score = score(user_cards)
                    if user_score > 21:
                        print(f"\tYour cards: {user_cards}, current score: {user_score}")
                        print(f"Computer's cards {computer_cards}")
                        print(f"\tComputer's first card: {computer_cards[0]}")
                        print("You lose")
                        game = False
                    elif user_score == 21:
                        print(f"\tYour cards: {user_cards}, current score: {user_score}")
                        print(f"Computer's cards {computer_cards}")
                        print(f"\tComputer's first card: {computer_cards[0]}")
                        print("You win by blackjack")
                        game = False
            elif chose == "n":
                on = True
                while on:
                    computer_cards += [card()]
                    computer_score = score(computer_cards)
                    if computer_score > user_score and computer_score == 21:
                        print(f"Your final hand {user_cards}, final score {user_score}")
                        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
                        print("You lose by Blackjack")
                        on = False
                    elif user_score < computer_score < 21:
                        print(f"Your final hand {user_cards}, final score {user_score}")
                        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
                        print("You lose")
                        on = False

                    elif computer_score > 21:
                        print(f"Your final hand {user_cards}, final score {user_score}")
                        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
                        print("You win")
                        on = False

                game = False
