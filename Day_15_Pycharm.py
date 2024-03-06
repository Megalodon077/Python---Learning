MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


penny = .01
nickel = .05
dime = .1
quarter = .25
money = 0


def calculate(item_cost):
    total_quarters = quarters * quarter
    total_dimes = dimes * dime
    total_nickles = nickles * nickel
    total_pennies = pennies * penny
    total_input_value = total_quarters + total_dimes + total_nickles + total_pennies

    if total_input_value >= item_cost:
        change = total_input_value - item_cost
        print(f"Here is ${round(change,2)} is change")
        return True
    elif total_input_value < item_cost:
        print("Sorry that's not enough money. Money is refunded.")
        return False


def is_left_resources(order_ingredients):
     for i in order_ingredients:
         if order_ingredients[i] >= resources[i]:
             print(f"Sorry, there is not enough {i} ! ")
             return False                                               #YES OR NO
     return True


def item(choice):
    if choice == "espresso":
        return MENU["espresso"]["cost"]
    elif choice == "latte":
        return MENU["latte"]["cost"]
    elif choice == "cappuccino":
        return MENU["cappuccino"]["cost"]

def make_coffe(drink_name, order_ingredient):
    for i in order_ingredient:
        resources[i] -= order_ingredient[i]


ask_coffee = True
while ask_coffee:
    choice = input("What would you like?(espresso/latte/cappuccino :  ") # TODO 1 : PROMPT FOR WHAT DO YOU WANT TO DRINK !
    if choice == "off":
        ask_coffee = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : ${money} ")
    else:
        drink = MENU[choice]
        if is_left_resources(drink["ingredients"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters? :"))
            dimes = int(input("How many dimes? :"))
            nickles = int(input("How many nickles? :"))
            pennies = int(input("How many pennies? :"))
            cost = item(choice)
            if calculate(item_cost=cost):
                make_coffe(choice, drink["ingredients"])
            print(f"Here is your {choice}. Enjoy !")

