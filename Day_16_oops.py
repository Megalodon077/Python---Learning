#Procedural programming - All the concepts that we did previous proojects
#Very confusing, here and there. Can create small program

#OOP, Object Oriented programming: A big task into smaller tasks
#attributes - variable(a modeled object) things that they have
#methods - funtions attached to an object(a modeled object can do) things that they do

#Create multiple version of same Object (CLASS) - BLUEPRINT]

#object      #class
#car = CarBlueprint()

from turtle import Turtle, Screen

timmy = Turtle()   #constructed an obejct from Class . Saved it in an object called Timmy
print(timmy)
timmy.shape("turtle")   #like functions
timmy.color("coral")
timmy.forward(100)


my_Screen = Screen()
my_Screen.canvheight    #object.attribute(variables)
print(my_Screen.canvheight)
my_Screen.exitonclick()


#Module - Some code file
#Packages - Lots and lots of Code


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu", "Squirtle", "Charmander" ])
table.add_column("Type",["Electric", "Water", "Fire"])  #methods
table.align = "l"   #attribute - changed style
print(table)

from prettytable import from_csv     #take CSV data and convrt to table
fp = open("C:\local\Test.csv", "r")
pt = from_csv(fp)
fp.close()
print(pt)