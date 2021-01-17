import random

def game():


    print("Welcome to the GUESSING NUMBER game")

    user_input = int(input("Whice number to start? "))
    user_input2 = int(input("Whice number to end? "))
    number = random.randrange(user_input, user_input2)

    print("Now you have 10 chanses to HIT the number...try")
    right = 1
    wrong = 1

    while wrong < 10:
        value = int(input("Enter your choosen number: "))
        try:
            response = int(value)
        except ValueError:
            print("Try again")
            continue
    
        if number > value:
            (6 - wrong)
            wrong = wrong + 1
            print("Lower number")
        
        elif number < value:
            (6 - wrong)
            wrong = wrong + 1
            print("Higher number")

        elif response == number:
            print("RIGHT, This is the correct number")
            break
    
    print("The number was", number)
    print("Thanks for playing my game!")

def main():
    game()

    while True:
        more_game = input("Do you want another game?(y/n) ")
        if more_game == "y":
            game()

        else:
            break
main()
print("Thanks for playing my game, wish you a good luck!")



