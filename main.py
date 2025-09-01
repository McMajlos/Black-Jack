import random
from art import logo, thanks
import os
from typing import List

cards: List[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

os.system("cls" if os.name == "nt" else "clear" )
print(logo)
start_game: str = input("Welcome to Blackjack game!\nDo you want to start? y/n ")

if start_game != "y":
    print("Alright, see you next time!")
    exit()


play_again: bool = True

def ask_again() -> bool:
    global play_again
    again: str = input("Do you want to play again? y/n ") 
    if again != "y":
        os.system("cls" if os.name == "nt" else "clear")
        print(thanks)
        play_again = False
    return play_again        


while play_again:
    os.system("cls" if os.name== "nt" else "clear")
    print(logo)
    your_cards: List[int] = random.choices(cards, k=2)
    dealer_cards: List[int] = random.choices(cards, k=1)
    print(f"Your cards are {your_cards} and the value is {sum(your_cards)}.")
    print(f"Dealer card is {dealer_cards}.")

    another_card: bool = True

    if sum(your_cards) == 21:
        print("\nBlackjack! You won!")
        another_card = False
        print("=" * 50)
        ask_again()
        

    while another_card:
        get_another_card: str = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_another_card == "y":
            your_cards.append(random.choice(cards))
            if sum(your_cards) > 21:
                print(f"Your cards after take {your_cards}")
                print(f"\nYou lost! Your cards value is {sum(your_cards)}.")
                another_card = False 
                print("=" * 50)
                ask_again()
            elif sum(your_cards) == 21:
                print(f"Your cards after take {your_cards}")
                print("\nYour cards value is 21! You won!")
                print("=" * 50)
                another_card = False 
                ask_again()
            elif sum(your_cards) < 21:
                print(f"Your cards are {your_cards} and the value is {sum(your_cards)}")
        else:
            print(f"\nYour final hand is {your_cards} and the value is {sum(your_cards)}.")
            if sum(dealer_cards) > sum(your_cards):
                print(f"Dealer cards are {dealer_cards} and the value is {sum(dealer_cards)}.")
                print("\nDealer won! Sorry... but that's life, right?")
                print("=" * 50)
                ask_again()
            elif sum(dealer_cards) == sum(your_cards):
                print(f"Dealer cards are {dealer_cards} and the value is {sum(dealer_cards)}.")
                print("\nIt's a DRAW!")
                print("=" * 50)
                ask_again()
            else:    
                while sum(dealer_cards) < sum(your_cards) and sum(dealer_cards) < 21:
                    dealer_cards.append(random.choice(cards))
                    if sum(dealer_cards) > 21:
                        print(f"Dealer cards after take {dealer_cards} and the value is {sum(dealer_cards)}.")
                        print(f"\nYou won!")   
                        print("=" * 50)
                        ask_again()
                    elif sum(dealer_cards) == sum(your_cards):
                        print(f"Dealer cards after take {dealer_cards} and the value is {sum(dealer_cards)}.") 
                        print("\nIt's a DRAW!")
                        print("=" * 50)
                        ask_again()
                    elif sum(dealer_cards) > sum(your_cards) and sum(dealer_cards) <= 21: 
                        print(f"Dealer cards after take {dealer_cards} and the value is {sum(dealer_cards)}.")      
                        print(f"\nDealer won! Sorry... but that's life, right?")
                        print("=" * 50)
                        ask_again()
            another_card = False    

    


