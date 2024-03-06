fruits = ["apple", "peach", "pear"]
for fruit in fruits:        #looping one by one items of the list and assigning it to "fruit" - each value is fruit now one by one
    print(fruit)
    print(fruit + "pie")

friends = ["but", "ran" ,"shaw"]
for new in friends:
    new = new + "lal"
    print(new)

#avg height without sum/len function:
student_height =input("Height of student : \n ").split()
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])
total_ht = 0
for h in student_height:
    total_ht += h                                  #total_ht = sum(student_height) - shortcut
print(f"total height is {total_ht} !")                  #if we indented it just under total_ht, it would give all the outputs one by one

total_student = 0
for students in student_height:
    total_student += 1                            #total_student = len(student_heights)
avg_ht = round(total_ht/total_student)
print(f"Avg ht of class is {avg_ht} ! ")

#Highest score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:                                 #max(students_score)
    if score > highest_score:
        highest_score = score
print(f"The heighest score in the class is: {highest_score}" )


#Range fuction : Till now we used "for" loop for only list, range function is useful "for" loop with individual vallues - how many time it will run the loop
for n in range(1,13,2):    #range(first number, last value before last included number, gap)
    print(n)

#sum of first n natural number :
total = 0
for n in range(1,101):
    total += n
print(total)

#Total of even number btw 1-100
total = 0
for n in range(2,101,2):
    total += n
print(total)

#OR

total2 = 0
for n in range(1,101):
    if n%2 == 0:
        total2 += n
print(total2)

#FIZZBUZ
for n in range(1,101):
    if n%3 == 0 and n%5 ==0:
        n = "FizzBuzz"
    elif n%5 ==0:
        n = "Buzz"
    elif n%3 ==0:
        n = "Fizz"
    print(n)

#random pypassword generator:

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = " "
for l in range(nr_letters):
    password+=random.choice(letters)
for n in range(nr_numbers):
    password+=random.choice(numbers)
for s in range(nr_symbols):
    password+=random.choice(symbols)
print(password)
choices = []
for c in password:
    choices.append(c)
random.shuffle(choices)
randpass = ""
for char in choices:
    randpass+=char
print(f"Your random password is {randpass}")




