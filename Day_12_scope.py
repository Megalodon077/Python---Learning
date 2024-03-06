# #SCOPE
#
# enemies = 1
#
# def increase_enemies():
#     enemies = 2          #inside the function enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function:{enemies}") #outside the function enemies = 1
#
#
# #Local scope
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(drink_potion())   #calling it outside the function - Local scope(inner)
#
# #Global scope
#
# player_health = 10 # - This becomes global scope as this was not mentioned under any function,
# #available inside and outside function
# def drink_potion():
#     potion_strength =2
#     print(player_health)
#
# drink_potion()
#
# #Namespace : naming the functions properly and only name
#
# #Modifying Global scope :
#
# l = 2
#
# def numbers():
#     global l
#     l +=1
#     print(l)
#
# #if you create a variable within a function it is only available within function - locally
# #if you creat a variuable within if, for, else, while, it is availably globa;lly
#
#
#
# #create global scopes with capitals



from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too High !")
        return turn - 1
    elif guess == answer:
        print("Too Low !")
        return turn - 1
    else:
       print(f"you got it ! The answer is {answer} !")

def set_difficulty():
    level = input("Choose a difficulty, 'easy' or 'hard' :\n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()


    guess = 0
    while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess !: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you loose ! ")
        return
    elif guess != answer:
        print("Guess again !")

game()



VS

from random import randint
number = randint(1, 100)
def hard_game(guess):
    attempts = 5
    game_on = True
    while game_on:
        if guess > number:
            print("Too high")
            attempts -= 1
        elif guess < number:
            print("Too low")
            attempts -= 1
        elif guess == number:
            game_on = False
            print("you win !")
            return

        print(f"You have {attempts} attempts left")
        if attempts != 0:
            guess = int(input("Guess again !\n"))
        elif attempts == 0:
            game_on = False
            print("You loose !")
def easy_game(guess):
    attempts = 10
    game_on = True
    while game_on:
        if guess > number:
            print("Too high")
            attempts -= 1
        elif guess < number:
            print("Too low")
            attempts -= 1
        elif guess == number:
            game_on = False
            print("you win !")
            return

        print(f"You have {attempts} attempts left")
        if attempts != 0:
            guess = int(input("Guess again !\n"))
        elif attempts == 0:
            game_on = False
            print("You loose !")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of number between 1 and 100.")
print(f"Pssst,the correct answer is {number}")
choice = input("Choose a difficulty. Type 'easy' or 'hard'\n")
if choice == "hard":
    print("You have 5 attempts")
    guess = int(input("Make a guess :\n"))
    hard_game(guess)
else:
    print("You have 10 attempts")
    guess = int(input("Make a guess :\n"))
    easy_game(guess)




