import random


#only use 4 lists, dont worry about having to have a specific place for each location
place_to_travel = ["San Antonio", "Las Vegas", "Orlando", "Denver"]
mode_to_travel = ["car", "train", "airline"]
place_to_eat= ["a brewpub", "The Hard Rock", "a fast food eatery", "a fine dining restaurant"]
thing_to_do = ["comedy club", "museum", "theatre", "movies"]


def trip_destination (place_to_travel):
    rand_destination = random.choice (place_to_travel) 
    print (f'Would you like to go to {rand_destination}? y or n?')
    user_destination_choice = input()
    if user_destination_choice != "y":
        trip_destination (place_to_travel)
    elif user_destination_choice == "y": 
        print ("Awesome, lets go!")
        return rand_destination
        
      
        
def travel_mode (mode_to_travel):
    rand_travel_mode = random.choice (mode_to_travel)
    print (f'Would you like to go by {rand_travel_mode}? y or n?')
    user_travel_mode_choice = input()
    if user_travel_mode_choice != "y":
        travel_mode (mode_to_travel)
    elif user_travel_mode_choice == "y": 
        print ("Great! Sounds fun!")
        return rand_travel_mode

    



def dinner_plans (place_to_eat):
    rand_food = random.choice (place_to_eat)
    print (f'Would you like to eat at {rand_food}? y or n?')
    user_food_choice = input()
    if user_food_choice != "y":
        dinner_plans (place_to_eat)
    elif user_food_choice == "y": 
        print ("Great! Sounds fun!")
        return rand_food
            
      

def entertainment_plans (thing_to_do):
    rand_entertainment = random.choice (thing_to_do)
    print (f'Would you like to go to the {rand_entertainment}? y or n?')
    user_entertainment_choice = input()
    if user_entertainment_choice != "y":
        entertainment_plans (thing_to_do)
    elif user_entertainment_choice == "y":
        print ("Fun Stuff!")
        return rand_entertainment


# add a variable infront of each function call, you will also need to make sure to add a return to each function 

confirmed_destination = trip_destination (place_to_travel)
confirmed_travel_mode = travel_mode (mode_to_travel)
confirmed_dinner_plans = dinner_plans (place_to_eat)
confirmed_entertainment_plans = entertainment_plans (thing_to_do)


# print (confirmed_destination)
# print (confirmed_travel_mode)
# print (confirmed_dinner_plans)
# print (confirmed_entertainment_plans)
print (f'Congratulations, youll be going to {confirmed_destination} by {confirmed_travel_mode}, where you will eat at {confirmed_dinner_plans} and then go to the {confirmed_entertainment_plans}')
