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
        if numbers[item[1]] == 1: 
            numbers[item[1]] = 11
            if sum + (numbers[item[1]]) > 21:
                numbers[item[1]] = 1
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
    
    time.sleep(2)
    os.system('cls')
    print("Your cards are: \n")
    print_cards(playerCards)
    print("\nYour Score is: ", calculateSum(playerCards))
    print("\nThe Dealer cards are: \n")
    print_cards(dealerCards)
    print("\nThe Dealer Score is: ", calculateSum(dealerCards), "\n")

    #Player Turn
    while calculateSum(playerCards) < 21:
        another_card = input(str("\nDo you want to HIT or Stand? (H / S) "))
        if another_card == "h":
            calculateSum(playerCards)
            draw_card(playerCards)
            os.system('cls')
            print("Your cards are: ")
            print_cards(playerCards)
            print("\nCalculating Score:" , calculateSum(playerCards), "\n")
            time.sleep(3)

        elif another_card == "s":
            print("\nCalculating Score...")
            time.sleep(2)
            print("\n-----------------------------")
            break

    if calculateSum(playerCards) > 21:
            return end_game("Player")
            
    #Dealer Turn
    while calculateSum(dealerCards) < 16:
        draw_card(dealerCards)
    os.system('cls')
    print("\nThe Dealer cards are: ")
    print_cards(dealerCards)
    print("\nThe dealer Score is: ", calculateSum(dealerCards), "\n")
    time.sleep(5)

    if calculateSum(dealerCards) > 21:
        return end_game("Dealer")

    if calculateSum(dealerCards) == 21:
        print("Dealer has BLACKJACK!!! Dealer Wins!")

    if calculateSum(dealerCards) < 21:
        if calculateSum(playerCards) > calculateSum(dealerCards):
            print("Your Score is: ", calculateSum(playerCards), ", And The Dealer Score is: ", calculateSum(dealerCards))
            if calculateSum(playerCards) == 21:
                print("You have BLACKJACK!!!")
            print("\nYou WIN!!! Take The MONEY!!!")

        elif calculateSum(playerCards) < calculateSum(dealerCards):
            print("Your Score is: ", calculateSum(playerCards), ", And The Dealer Score is: ", calculateSum(dealerCards))
            print("\nDealer WINS! You LOSE...The MONEY has gone...")

        elif calculateSum(playerCards) == calculateSum(dealerCards):
            print("Your Score is: ", calculateSum(playerCards), ", And The Dealer Score is: ", calculateSum(dealerCards))
            print("\nNow that is a TIE!")

        
def end_game(whichDeck):
    print(whichDeck, "lose...More Than 21...")

def main():
    gameplay()

main()    