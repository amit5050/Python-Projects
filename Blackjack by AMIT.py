#Blackjack
import random
import time

playerCards = []
dealerCards = []
deck = []
symbols = {"Hearts":"♥","Spades":"♠","Clubs":"♣","Diamonds":"◆"}
numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"j":10,"q":10,"k":10}

    
def printCard():
    for symbol in symbols:
        for number in numbers:
            deck.append("{}" "{}".format(number, symbol))
    random.choice(deck)

    print("""
    ------------
    | {}      {} |
    |          |
    |          |
    | {}      {} |
    ------------
    """.format(symbols[symbol],numbers[number],numbers[number],symbols[symbol]))

printCard()