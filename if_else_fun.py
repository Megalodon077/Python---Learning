def max(num1, num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return  num3

print(max(23,45,34))

num1 = float(input("Enter first number :\n"))
op = input("Select your op : \n")
num2 = float(input("Enter Second number :\n"))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid op")


