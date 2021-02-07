#Blackjack
import random
import time
import os

os.system('cls')

playerCards = []
dealerCards = []
deck = []
symbols = {"Hearts":"♥","Spades":"♠","Clubs":"♣","Diamonds":"◆"}
numbers = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

def create_cards(card):
    [symbol, number] = card
    weight_card = 12
    height_card = 8
    
    card_weight_top = ' ' + ('_' * weight_card)
    print(card_weight_top)
    for h in range(height_card):
        if h == 1:
            print('| ', symbol, '\t ', number,' |')
        if h == 7:
            print('| ', number, '\t ', symbol,' |')
        print('|\t     |')
    card_weight_bottom = ' ' + ('_') * weight_card
    print(card_weight_bottom)

    return symbol, number

def create_deck():
    for symbol in symbols.values():
        for number in numbers.keys():
            deck.append([symbol, number])
    random.shuffle(deck)
    
create_deck()

def draw_card(whichDeck):
    whichDeck.append(create_cards(deck.pop()))

def print_cards(array):
    for item in array:
        create_cards(item)

def calculateSum(array):
    sum = 0
    for item in array:       
        sum += numbers[item[1]] 
    return sum

def initiate():
    print("Welcome To BLACKJACK!")

    print("Player cards: \n")
    time.sleep(2)
    draw_card(playerCards)
    print("\n-----------------------------")
    print("\n Dealer cards: \n")
    time.sleep(2)
    draw_card(dealerCards)
    print("-----------------------------")
    print("\n Player cards: \n")
    time.sleep(2)
    draw_card(playerCards)

initiate()

def gameplay():
    #Player Turn
    time.sleep(2)
    os.system('cls')
    print("Your cards are: \n")
    print_cards(playerCards)
    print("\nYour Score is: ", calculateSum(playerCards))

    while calculateSum(playerCards) < 21:
        another_card = input(str("\nDo you want to draw one more card? (y / n) "))
        if another_card == "y":
            draw_card(playerCards)
            os.system('cls')
            print("Your cards are: ")
            print_cards(playerCards)
            print("\nCalculating Score:" , calculateSum(playerCards), "\n")

        elif another_card == "n":
            print("\nCalculating Score...")
            time.sleep(2)
            print("\n-----------------------------")
            break
            
    #Dealer Turn
    while calculateSum(dealerCards) < 16:
        print("\nThe Dealer cards are: ")
        draw_card(dealerCards)
        print_cards(dealerCards)
        print("\nThe dealer Score is: ", calculateSum(dealerCards))
        time.sleep(5)

    if calculateSum(playerCards) > calculateSum(dealerCards):
        print("Your Score is: ", calculateSum(playerCards), ", And The Dealer Score is: ", calculateSum(dealerCards))
        print("\nYou WIN!!! Take The MONEY!!!")

    elif calculateSum(playerCards) < calculateSum(dealerCards):
        print("Your Score is: ", calculateSum(playerCards), ", And The Dealer Score is: ", calculateSum(dealerCards))
        print("\nYou LOSE...The MONEY has gone...")

    elif calculateSum(playerCards) == calculateSum(dealerCards):
        print("Your Score is: ", calculateSum(playerCards), ", And The Dealer Score is: ", calculateSum(dealerCards))
        print("\nNow that is a TIE!")

def main():
    gameplay()
    play_again = input(str("Do you wanna play again? (y / n) "))
    while play_again == 'y':
        print("Starting...")
        time.sleep(3)
        create_deck()
        initiate()
        gameplay()

        
    print("Good Bye...")

main()    