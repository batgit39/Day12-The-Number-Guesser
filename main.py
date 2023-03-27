import os, random
from art import logo

def checker(users_guess, answer):
    if users_guess == answer:
        print("Bravo you guessed the number!")
        return True
    else:
        if users_guess > answer:
            os.system('clear')
            print(logo)
            if users_guess - answer >= 20:
                print("Your guess is too high\n")
            elif users_guess - answer >= 10:
                print("Your guess is bit high\n")
            elif users_guess - answer >= 5:
                print("A little bit lower\n")
            elif users_guess - answer >= 2:
                print("You are almost there just a bit low\n")    
            else:
                print("You are very close\n")
            
            
        elif users_guess < answer:
            os.system('clear')
            print(logo)
            if answer - users_guess >= 20:
                print("Your guess is too low\n")
            elif answer - users_guess >= 10:
                print("Your guess is bit lower\n")
            elif answer - users_guess >=  5:
                print("A little bit higher\n")
            elif answer - users_guess >= 2:
                print("You are almost there just a bit higher\n")    
            else:
                print("You are very close\n")

def game():
    os.system('clear')

    #getting random number
    answer = random.randint(1, 100)
    # print(answer)

    print(logo)
    print("Welcome to the game!")
    print("I am thinking of a number between 1-100 try to guess that number")
    difficulty = input("Choose Difficulty\nEasy - 10 lives - e\nHard - 5 lives - h : ").lower()
   

    if difficulty == "e":
        x = True
        lives = 10
        while x:
            if lives == 0:
                print("You lost!")
                break
            else:
                users_guess = int(input("Guess the number : "))
                if checker(users_guess, answer):
                    x = False
                else:
                    lives -= 1
                    print(f"{lives} lives left.")

    elif difficulty == "h":
        x = True
        lives = 5
        while x:
            if lives == 0:
                print("You lost!")
                break
            else:
                users_guess = int(input("Guess the number : "))
                if checker(users_guess, answer):
                    x = False
                else:
                    lives -= 1
                    print(f"{lives} lives left.")
    else:
        y = input("Wrong input, Press any button to try again.")
        game()

game_loop = True
while game_loop:
    os.system('clear')

    if input("To play a game press y : ").lower() != "yes":
        game()
        game_loop = False
