def greet():         #DEFINING SIMPLE FUNCTION
  print("Hello Devansh")
  print("How do you do Devansh ?")
  print("Isn't the weather nice today?")

greet()

#fUNCTION THAT ALLOWS INPUT
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}")

greet_with_name("Dev")

#something = 123
#something = parameter = name of the data
#123 = argument = true data/actual data

#FUNCTION WITH MORE THAN 1 INPUT
def greet_with(name, location):
  print(f"Hello {name} !")
  print(f"what is it like in {location}")

greet_with("Devansh", "Hyderabad")   #positional argument
greet_with(location="HYD", name="Dev")   #keyword argument


#Paint needed :
from math import *
def paint_calc(height, width, cover):
    num_of_cans = ceil((height*width)/coverage)
    print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#PRIME NUMBER CHECKER
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:    #checker : use brain
            is_prime = False
    if is_prime:
        print("Its a prime number")
    else:
        print("Its not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)


#caeser_game
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):    #defining caeser function
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char   #for the random characters
    print(f"Here's the {cipher_direction}d result: {end_text}")

# from art import logo
# print(logo)
caeser_is_on = True
while caeser_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26        # remainder
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice = input("Do you want to play this more ? ")
    if choice == "no":
        caeser_is_on = False
        print("You have exited")

