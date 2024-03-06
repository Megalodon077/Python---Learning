#Modules: different functions
import random
random_int = random.randint(1,10)                         #"random" is modeule: which is a program already written somewhere and is stored. We import it to do some function
print(random_int)                                         #"random.randit- calling"randit" funcion : gives random number btw(num1,num2)

random_flt = random.random()                              #calling for "random" fun from random module - will give flt number btw[0,1)
print(random_flt)

#print random flt btw[0,5)
random_flt2 = random_flt * 5
print(random_flt2)

#love calc - its not actual scienece so why not print random number :
love_score = random.randint(1,100)
print(f"You love score is {love_score} <3")

#Heads or tails
import random
random_num = random.randint(1,2)
if random_num == 1:
    print("Heads")
elif random_num ==2:
    print("Tails")


#Lists: Data structure: organising & storing data(more than single data)
#similar type of data or different
#store it a order

states_of_india = ["Himachal","Punjab","Telangana","Andhra Pradesh","Maharashtra","Goa","Manipur","Meghalaya"]
print(states_of_india[-1])                           #finds out the value on that index
states_of_india[-1] = "Megalodon"                    #changes value on that index
print(states_of_india)
states_of_india = states_of_india + ["Gujrat"] #or states_of_india.append("Gujrat")  append function: adds a value to the list in the end
states_of_india.extend(["Rajasthan","Jharkhand","Uttar Pradesh"])    #extend function will add a list of values !
print(states_of_india)
states_of_india.insert(1,"Haryana")
print(states_of_india)


#random bill
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")                                             #creates an array["name1","name2",etc]
l = len(names)                                                              #finds out the number of characters for indexing
defaulter = random.randint(0,l-1)                                           #choose random index
unlucky_guy = names[defaulter]                                              #choose name from random index
print(f"{unlucky_guy} will have to pay ! ")
#OR
import random
names_string = input("Give me the names with ',' separated :\n")
names = names_string.split(",")
unlucky_guy = random.choice(names)                 #short cut to pick choice
print("Unlucky person is " + unlucky_guy)

#nested_LIsts
Footballers = ["messi","ronaldo","haaland","mbappe","Ibra"]
Cricketers = ["Dhoni","Kohli","Sachin","Sehwag","Gill"]
Sports_personalities = [Footballers, Cricketers]
print(Sports_personalities)

#assign a character an index in the matrix ! (column,row)
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")                #this is equal to map
position = input("Where do you want to put the treasure? ")
x = int(position[1])
y = int(position[0])
map[x-1][y-1] = "x"
print(f"{row1}\n{row2}\n{row3}")

#rock,paper and scissors: This may cause error:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choices = [rock, paper, scissors]
your_choice = input("rock, paper, scissor : \n")
if your_choice != "rock" or your_choice !="paper" or your_choice != scissors:
    print("Invalid input, you loose !")
if your_choice == "rock":
    print("Your choice")
    print(rock)
    random_choice = random.randint(0, 2)
    computer_choice = choices[random_choice]
    print("Computer choice")
    print(computer_choice)
    if computer_choice == scissors:
        print("You win !")
    elif computer_choice == paper:
        print("You loose")
    else:
        print("Its a draw")

if your_choice == "paper":
    print("Your choice")
    print(paper)
    random_choice = random.randint(0, 2)
    computer_choice = choices[random_choice]
    print("Computer choice")
    print(computer_choice)
    if computer_choice == scissors:
        print("You loose !")
    elif computer_choice == paper:
        print("Its a  draw !")
    else:
        print("You win !")

if your_choice == "scissors":
    print("Your choice")
    print(scissors)
    random_choice = random.randint(0, 2)
    computer_choice = choices[random_choice]
    print("Computer choice")
    print(computer_choice)
    if computer_choice == scissors:
        print("Its a draw !")
    elif computer_choice == paper:
        print("You Win !")
    else:
        print("You loose !")

#alternative formula for rock paper:
choices = [rock, paper, scissors]
user_choice = int(input("What do you choose ? Enter 0 for rock, 1 for paper & 2 for scissors "))
if user_choice > 3 or user_choice < 0:
    print("You have input an invalid numer, you Loose !")
else:
    print("Your choice is :")
    print(choices[user_choice])
    computer_choice = random.choice(0,2)
    print("Computer choice is : ")
    print(choices[computer_choice])

    #create - different scenarios similar to line 151



