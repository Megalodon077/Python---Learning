import random
friends = ["Dhruv", "Srini", "Kuki", "Ishan"]

print(friends[1:]) #from 1 to end

print(friends[:2]) #from begining to the "2-1" last not included evr

friends[2] = "Arch"  # added



#LIST FUNCTIONS

friends.extend(["misba","nikita"])    #extend works on a list

friends.append("Siddhant")

friends.insert(1, "Kaps")

friends.remove("Kaps")

friends.clear()   #clears the list

friends.pop()  # clears the last element of the list

friends.index("misba"))  #index of misba

friends.count("misba")   #no of "misba"

friends.sort()  #ascending order

friends.reverse()

friends2 = friends.copy()

print(friends)

