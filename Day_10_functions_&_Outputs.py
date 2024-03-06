def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"  #OUTPUT RETURN KEYWORD

print(format_name("dEvansh", "RANA"))    #OUTPUT REPLACES CALLED FUNCTION


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



#Calculator

# Add
def add(n1,n2):
    return n1 + n2
# Subtract
def subtract(n1,n2):
    return n1 - n2
# Multiply
def multiply(n1,n2):
    return n1 * n2
# Divide
def divide(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "_" : subtract,
    "*" : multiply,
    "/"   : divide,
}
def calculator():  #recurssion
    num1 = int(input("What's the first number? : "))
    for symbol in operation:
        print(symbol)
    calculations = True

    while calculations:
        operation_symbol = input("Pick an operation ")
        num2 = int(input("What's the next number? :"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. : ")
        if choice == "y":
            num1 = answer
        else:
            calculations = False


calculator()





