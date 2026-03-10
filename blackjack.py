import random

MIN_BET = 10
MAX_BET = 100

characters_digit = 2, 3, 4, 5, 6, 7, 8, 9
character_picture = {"King": 10, "Queen": 10, "Joker": 10, "Ace": 11}

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

def main():
    bet = get_bet()
main()
