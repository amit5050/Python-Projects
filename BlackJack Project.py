import random
import time

class BlackJack:
    def __init__(self):
        self.lost = "lost"
        self.won = "won"
        self.blackjack = "blackjack"
        self.playerMoney = 100
        self.deckOfCards = []
        self.playerCards = []
        self.dealerCards = []
        self.symbols = {"Hearts":"♥","Spades":"♠","Clubs":"♣","Diamonds":"◆"}
        self.numbers = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"j":10,"q":10,"k":10}


    def createDeck(self):
        for symbol in self.symbols:
            for number in self.numbers:
                self.deckOfCards.append("{} {}".format(number,symbol))
        
        random.shuffle(self.deckOfCards)


    def printCard(self,card):
        [number,symbol] = card.split()
        print("""
        ------------
        | {}      {} |
        |          |
        |          |
        | {}      {} |
        ------------
        """.format(self.symbols[symbol],self.numbers[number],self.numbers[number],self.symbols[symbol]))

    def printCards(self,array):
        for item in array:
            self.printCard(item)
        print("cards sum: {}\n".format(self.calculateSum(array)))
        
            

    def drawCard(self,whichDeck):
        whichDeck.append(self.deckOfCards.pop())



    def calculateSum(self,array):
        numberSum = 0
        for item in array:
            [number,value] = item.split()
            if number == "one" and numberSum + 11 <= 21:
                numberSum += 11
            else:
                numberSum += self.numbers[number]
        return numberSum

        

    def initiate(self):
        self.drawCard(self.playerCards)
        self.drawCard(self.dealerCards)
        self.drawCard(self.playerCards)
        print("Your cards are:")
        self.printCards(self.playerCards)
        time.sleep(3)
        print("Dealer cards are:")
        self.printCards(self.dealerCards)


    def gameplay(self):
        if self.calculateSum(self.playerCards) == 21:
            print("You Have BLACKJACK!!! You WIN!!!")
            return self.blackjack 

    #player turn
        while (self.calculateSum(self.playerCards) <= 21):
            userAnswer = input("Do you want to draw another? y/n: ")
            print("...")
            time.sleep(1.5)
            if userAnswer.lower() == "y":
                self.drawCard(self.playerCards)
                self.printCards(self.playerCards)
                if(self.calculateSum(self.playerCards) > 21):
                    print("You lost mate!")
                    return self.lost 
            else:
                break
    #dealer turn
        while (self.calculateSum(self.dealerCards) <= 16):
            print("Dealer starting to draw cards now")
            time.sleep(0.5)
            print("...")
            time.sleep(2)
            self.drawCard(self.dealerCards)
            self.printCards(self.dealerCards)
            if self.calculateSum(self.dealerCards) > 21:
                 print("You won!! The dealer lost!")
                 return self.won

        print("Calculating score....")
        time.sleep(2.5)

        if self.calculateSum(self.dealerCards) > self.calculateSum(self.playerCards):
            print("You lost ALL THE MONEY!!")
            return self.lost
        elif self.calculateSum(self.dealerCards) < self.calculateSum(self.playerCards):
            print("You won!!#!@ wowowowoowowww")
            return self.won
        else:
            print("No one wins!!!!!")


    def start(self):
        print("Welcome to blackJack")
        print("You Have", self.playerMoney, "$")
        self.playerCards = []
        self.dealerCards = []
        time.sleep(2)
        money = -1
        while money == -1 or money >= self.playerMoney:
            money = int(input("How much money do you want to gamble with?: $"))
            if money >= self.playerMoney:
                print("Not enough funds")
        
        start.createDeck()
        start.initiate()
        gameState = start.gameplay()
        if gameState == self.won:
            self.playerMoney += money
        if gameState == self.lost:
            self.playerMoney -= money
        if gameState == self.blackjack:
            self.playerMoney += money * 1.5
        
        print("You have {} $ right now".format(self.playerMoney))

        startAgain = str(input("Do you want to play another? y/n: "))
        if startAgain.lower() == "y":
            self.start()

            

start = BlackJack()
start.start()


