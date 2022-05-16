import random



place_to_travel = ["San Antonio", "Las Vegas", "Orlando"]
mode_to_travel = ["Rental Car", "Train", "Airline"]
place_to_eat_LAS = ["Luxor", "MGM", "Bellagio"]
place_to_eat_SAT = ["Mi Tierra", "Mon Chu Chu", "ChartHouse"]
place_to_eat_ORL = ["Bubba Gump", "House of Blues", "Millers Ale House"]
thing_to_do_LAS = ["Cirque Show", "Pawn Stars", "High Roller"]
thing_to_do_SAT = ["Alamo", "River Walk", "The Pearl"]
thing_to_do_ORL = ["Disney", "Universal", "Hard Rock"]

def trip_destination (place_to_travel):
    rand_destination = random.choice (place_to_travel) 
    print (f'Would you like to go to {rand_destination}? y or n? ')
    user_destination = input()
    if user_destination != "y":
        trip_destination (place_to_travel)
    elif user_destination == "y": 
        print ("Awesome, lets go!")
        
      
        
# def travel_mode (mode_to_travel):
#     rand_travel_mode = random.choice (mode_to_travel)
#     print (f'Would you like to go by {rand_travel_mode}?')
#     travel_mode_choice = input("y or n? ")
#     if travel_mode_choice != "y":
#         travel_mode (mode_to_travel)
#     elif travel_mode_choice == "y": 
#         print ("Great! Sounds fun!")
    

# # need to apply random selction based on destination

# def dinner_plans_vegas (place_to_eat_LAS):
#     if travel_mode == "Las Vegas":
#         rand_eatery = random.choice (place_to_eat_LAS)
#         print (f'Would you like to eat at {rand_eatery}')
        # LAS_eatery_choice = input ("y or n? ")
        #     if LAS_eatery_choice != "y":
        #         dinner_plans (place_to_eat_LAS)
            
    

# # need to apply random selection based on destination   

# def entertainment_plans (entertainment_places):
#     rand_entertainment = random.choice (entertainment_places)
#     print (rand_entertainment)

trip_destination(place_to_travel)
# travel_mode (mode_to_travel)
# dinner_plans (place_to_eat_LAS)
# entertainment_plans (thing_to_do_LAS)
