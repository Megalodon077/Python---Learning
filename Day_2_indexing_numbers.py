print("hello"[0])                 #[]: indexed value
num_char = len(input("whats your name ? "))
print("you name has " +str(num_char) + " characters ! ")     #num_char is an integer therefore had to convert it to string to add with other strings


#ADD NUMBERS OF A TWO DIGIT NUMBER
two_digit_num = input(("Enter a number :\n"))
x = int(two_digit_num[0])
y = int(two_digit_num[1])
result = x + y
print(result)

#BMI CALCULATOR
H = float(input("enter your height :\n"))
W = int(input("enter your weight :\n"))
BMI = int(W/H**2)
print(BMI)

print(8/3)
print(int(8/3))     #int value
print(8//3)         #direct method without convetting to int value = FLOW DIVISION
print(round(8/3))      #round to the closest int
print(round(8/3,2))     #round to the required decimal value

result = 4/2
result *= 2           #store a value in a variable and then manupilate /=, *=, +=, -=
print(result)

score = 100
height = 1.8
isWinning = True
#f-string : Do not have to convert data types to strings - add "f" in front of string
print(f"your score is {score}, your height is {height}, your chances of winning is {isWinning}")

#your age in months, weeks, days
age = input("Tell us your age :\n")
remaining_age = 90 - int(age)
remaining_days = remaining_age * 365
remaining_weeks = remaining_age * 52
remaining_months = remaining_age * 12
print(f"You are left with {remaining_days} days or {remaining_weeks} weeks or {remaining_months} months.\nSO, What are you waiting for ??")

#Bill split
bill = int(input("enter bill :\n"))
Tip = int(input("How much tip? 10,12,15 ?\n"))
people = int(input("How many people"))
Final_ind_bill = (bill*(1 + Tip/100))/5
print(round(Final_ind_bill,2))







