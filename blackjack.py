from replit import clear
from art import logo
import random 
def ending():
    """This will ask the user if he wants to continue the game or not"""
    end = input("Do you want to play again press 'Y' for yes or press 'N' for no : ")
    ending = end.lower()
    if ending == "n":
        x = 20
        return(x)
def comparing(y_card , c_card):
    """This will compare the total and show the result if user win,lose or had a draw"""
    total1 = sum(y_card)
    total2 = sum(c_card)
    if total1 ==21:
        print("You won directly by blackjack(0)")
        return
    if total2 ==21:
        print("Computer won by blackjack(0)")
        return
    if 21-total1 > 21-total2:
        print("YOU LOSE!!!")
    elif 21-total1 == 21-total2:
        print("ITS A DRAW !") 
    else:
        print("YOU WIN !!!!!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
starting = True
start = input("Do you want to play game ,press 'Y' for yes and press 'N' for no: ")
star = start.lower()
while starting == True:
    clear()
    print(logo)
    your_card = []
    computer_card = []
    randomizer1 = random.randrange(0,12)
    randomizer2 = random.randrange(0,12)
    randomizer3 = random.randrange(0,12)
    randomizer4 = random.randrange(0,12)
    computer_card.append(cards[randomizer1])
    your_card.append(cards[randomizer3])
    your_card.append(cards[randomizer4])
    print(f"Your cards are : {your_card}")
    print(f"Computer's first card is : {computer_card}")
    computer_card.append(cards[randomizer2])
    wan1 = input("Do you  want to pick another card press 'Y' for yes or press 'n' for no  : ")
    want1 = wan1.lower()
    if want1 == "n":
        print(f"Your cards are : {your_card}")
        print(f"Computers cards are : {computer_card}")
        comparing(your_card,computer_card)
        end = ending()
        if end == 20:
            starting = False
    else:
        randomizer5 = random.randrange(0,12)
        your_card.append(cards[randomizer5])
        total = sum(your_card)
        if total>21 and 11 in your_card:
                your_card.remove(11)
                your_card.append(1)
                total = sum(your_card)
        if total > 21:
            print(f"Your cards are : {your_card}")
            print(f"Computers cards are : {computer_card}")
            print("YOU LOSE !!!")
            end = ending()
            if end == 20:
                starting = False
        if total < 21 and total>=17:
            print(f"Your cards are : {your_card}")
            print(f"Computers cards are : {computer_card}")
            comparing(your_card,computer_card)
            end = ending()
            if end == 20:
                starting = False
        while total < 17:
            print("you have to take a card until its grater than 17: ")
            randomizer6 = random.randrange(0,12)
            your_card.append(cards[randomizer6])
            total = sum(your_card)
            if total>21 and 11 in your_card:
                your_card.remove(11)
                your_card.append(1)
                total = sum(your_card)
            if total>21:
                print(f"Your cards are : {your_card}")
                print(f"Computers cards are : {computer_card}")
                print("YOU LOSE!!!!")
                end = ending()
                if end == 20:
                    starting = False
            if total < 21:
                print(f"Your cards are : {your_card}")
                print(f"Computers cards are : {computer_card}")
                comparing(your_card,computer_card)
                end = ending()
                if end == 20:
                    starting = False
else:
    print("THANKS, HAVE A GOOD DAY :) ")               



        
            



