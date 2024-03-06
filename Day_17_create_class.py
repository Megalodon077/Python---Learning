class User:          #all names capital (pascal case)
    def __init__(self):   #to initialize an attribute
        print("New user is being constructed")

user_1 = User()
user_1.id = "001"  # id = attribute
user_1.username = "rana" # username = attribute

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.name = "devansh"