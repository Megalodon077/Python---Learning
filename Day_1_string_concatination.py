print("Devansh\nrana")
print("devansh" + " rana")        #concatination
print('de')                                       #indentation error - add space before code
                                                         #syntax error : miss something

print("Hey " + input("Your name : "))                             #NESTING

print(len(input("whats your name? ")))         #nesting

name = input("name :")                     #another way, can store function in variable
lenth = len(name)
print(lenth)

                                                    #variable_naming - len1,len2 but not 1len or 2len
#c =a
#a=b
#b=c         this is how you can interchange values

#BAND NAME

print("Hey Guys, what's up? Ready to create a band name ? ")
city = input("Which city you grew up in ?\n ")
pet = input("whats the name of your pet ?\n ")
print("your band name is " + city+ " " +pet)        #REMEBER: "+", concatination has worked here as this is same data type - string