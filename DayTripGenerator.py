"""
 As a developer, I want to store my destinations, restaurants, 
 mode of transportation, and entertainment in their own separate Lists. 
 """
Destinations = ["Miami", "Italy", "Egypt", "Atlanta"]
Restuarnts = ["Longhorns", "Olive Garden", "Zaxbys", "American Deli"]
Modes_of_Transportations = ["Car", "Plane", "Train", "Cruise"] 
Entertainments = ["Concert", "Skydiving","Hiking", "Spa"]

"""
As a user, I want a destination to be randomly selected for my day trip. 
"""
# Destinations = ["Miami", "Italy", "Egypt", "Atlanta"]
# print(Destinations[0])

'''
As a user, I want a Restuarant to be randomly selected for my day trip.
'''
# Restuarnts = ["Longhorns", "Olive Garden", "Zaxbys", "American Deli"]
# print(Restuarnts[0])
'''


As a user, I want a mode of transportation to be randomly 
selected for my day trip
'''
# Modes_of_Transportations = ["Car", "Plane", "Train", "Cruise"]
# print(Modes_of_Transportations[0])
'''


As a user, I want a form of entertainment to be randomly
selected for my day trip.
'''
# Entertainments = ["Concert", "Skydiving","Hiking", "Spa"]
# print(Entertainments[0])

# print(Destinations[1], Entertainments[1], Modes_of_Transportations[1], Restuarnts[1]) 
# print(Destinations[2], Entertainments[2], Modes_of_Transportations[2], Restuarnts[2]) 
# print(Destinations[3], Entertainments[3], Modes_of_Transportations[3], Restuarnts[3])
'''
As a user, I want to be able to randomly
re-select a destination, restuarant, mode of transporation
and/or form of entertainment if I don't like one or more of those things
'''
Destinations = ["Miami", "Italy", "Egypt", "Atlanta"]

# print(Destinations[0], Entertainments[0], Modes_of_Transportations[0], Restuarnts[0])

# likes_random_choices = input("Did you like this option? y/n ")
   
# if likes_random_choices == 'n':    
#      print("Let's try another one.")
   
# elif likes_random_choices == 'y':
#     print("Awesome choice!")
    
# else:    
#      print("Sorry! Please choose one of the given options")


'''
As a user, I want to be able to confirm that my day 
trip is “complete” once I like all of the random selections.
'''
# trip_confirmed = input("Do you like all of your selections? y/n ")

# if trip_confirmed == "y":
#     print("Your day trip is complete")
# else:
#     print("Sorry to hear, try starting over")

def random_generator():
    random_destination = Destinations
    random_mode = Modes_of_Transportations
    random_ent = Entertainments
    random_rest = Restuarnts
    # get and hold randitem
    # get and hold randMode 
    # get and hold randEnt
    # get and hold randRest
    # return all 4 items in a collection (list)
    return []

def app():
    rand= random_generator()