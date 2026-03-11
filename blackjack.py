import random

MIN_BET = 10
MAX_BET = 100
BLACKJACK = 21

all_cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

def get_bet():
    while True:
        amount = input("How moch do you wanna bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"\nYou only can bet between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a valid number. ")
    return amount

def get_hand():
    global hand_value
    first_card = random.choice(list(all_cards.keys()))
    second_card = random.choice(list(all_cards.keys()))
    hand_value = all_cards[first_card] + all_cards[second_card]

    print(f"\nCards: [{first_card}] - [{second_card}]")
    print(f"Hand Value: {hand_value}.")

    return hand_value

def get_hand_dealer():
    first_card = random.choice(list(all_cards.keys()))
    dealer_hand = all_cards[first_card]
    dealer_value = dealer_hand
    print(f"\nDealers Card: [{dealer_hand}].")
    print(f"Dealers Value: {dealer_value}.")

    return dealer_value


def new_card(hand_value):
    while True:
        new_card = input("New Card?: [y] - [n]: ")
        if new_card == "n":
            break
        elif new_card == "y":
            card = random.choice(list(all_cards.keys()))
            card_value = all_cards[card]

            hand_value = (hand_value + card_value) % 100

            print(f"\nNew Card: [{card}]")
            print(f"Hand Value: {hand_value}.")
        else:
            break
    return hand_value

def check_winner(new_value, dealer_value):
    if new_value == 21:
        print("BLACKJACK! You win.")
    elif new_value > 21:
        print("Above 21. You lose.")
    elif dealer_value > 21:
        print("Dealer bust! You win.")
    elif new_value > dealer_value:
        print("You win!")
    elif new_value < dealer_value:
        print("You lose.")
    else:
        print("It's a tie.")

def main():
    bet = get_bet()
    hand_value = get_hand()
    dealer_value = get_hand_dealer()
    new_value = new_card(hand_value)
    winner = check_winner(new_value, dealer_value)

main()
