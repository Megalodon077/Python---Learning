programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again." ,
}
print(programming_dictionary["Bug"])

#adding new items to dictionary.
programming_dictionary["Vawzen"] = "eminent"
print(programming_dictionary)

#Create an empty dictionary.
empty_dictionary = {}

#Wipe a dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an iten in a disctionary
programming_dictionary["Bug"] = "Sup ?"
print(programming_dictionary)

#Loop through a dictionary
for thing in programming_dictionary:
  print(thing)
  print(programming_dictionary[thing])


#Grading system
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for i in student_scores:
  score = student_scores[i]
  if score >= 91 and score < 100:
    grade = "Outstanding"
  elif score >= 81 and score < 90:
    grade = "Exceeds Expectations"
  elif score >= 71 and score < 80:
    grade = "Acceptible"
  else:
    grade = "Fail"
  student_grades[i] = grade

print(student_grades)

#OR
student_grades = {}
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)



#Nesting
Capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

#Nesting a List in a Dictionary
Travel_log = {
  "France" : ["Paris", "Lille", "Dijon"],
  "Germany": ["berlin", "Hamburg", "Stuttgart"]
}

#Nesting a Dictionary in a Dictionary
Travel_log = {
  "France" : {"Cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},  #Curly brackets important !!!
  "Germany": {"Cities_visited": ["berlin", "Hamburg", "Stuttgart"], "total_visits" : 5},
}

#Nesting a Dictionary in a List
Travel_log = [
  {
   "Country" : "France",
   "Cities_visited" : ["Paris", "Lille", "Dijon"],
   "total_visits" : 12
  },  #Curly brackets important !!! #Each dictionary has 3 key value pair
  {
   "Country": "Germany",
   "Cities_visited": ["berlin", "Hamburg", "Stuttgart"],
   "total_visits" : 5
  },
]


#Nesting dictionary to list of travel_log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited,times_visited,cities_visited): #defined function with parameters
    new_country = {}
    new_country["country"] = country_visited   #adding to the list
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#Bidding game
from replit import clear
from art import logo
print(logo)
Name_bid = {}
bidding = True
def find_winner(bidding_record):      #how winning
  highest_bid = 0     #to compare
  champion = ""   #to addd champion
  for i in bidding_record:
    bid_amount = bidding_record[i]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      champion = i
  print(f"The winner is {champion} with a bid of {highest_bid}")

while bidding:
  Name = input("What is your name?\n")
  Bid = int(input("Please enter your bid?\n"))
  Name_bid[Name] = Bid
  choice = input("Are there other biders ? ").lower()
  if choice == "no":
    bidding = False
    find_winner(bidding_record=Name_bid)
  elif choice == "yes":
    clear()