# # ## Ask the user for 3 favorite Nigerian dishes
# # dish1 = input("Enter your first favorite Nigerian dish: ")
# # dish2 = input("Enter your second favorite Nigerian dish: ")
# # dish3 = input("Enter your third favorite Nigerian dish: ")
# # dishes = (dish1, dish2, dish3) ## Store them in a tuple called dishes
# # print(":", ", ".join(dishes)) # Print the tuple in a single line, separating items with commas
# # print("\nYour favorite dishes are :")
# # for dish in dishes:
# #     print(dish)
# # print(" God bless you for coming tom us")

#       # TASK 2 TUPLE AND INPUT
# #    task2: Tuple and Input ####
# #    Ask the user for 5 best friends’ names.
# #    Store them in a tuple friends.
# #    Print the tuple in reverse order.

# # step 1  :>>>>> Initialize an empty list to store the names temporarily
# friend_Best5_names_list = []
# #  STEP 2 :>>>>>>Ask the user for 5 best friends' names
# name_1 = input("Enter the name of your best friend :")
# name_2  = input("Enter name The second name:")
# # name_3  =input("Next name :")
# # name_4 = input(" Next name :")
# # name_5 = input(" last name :")
# # # # Convert the list to a tuple
# # friend_Best5_names_list.append(name_1)
# # friend_Best5_names_list.append(name_2)
# # friend_Best5_names_list.append(name_3)
# # friend_Best5_names_list.append(name_4)
# # friends = tuple(friend_Best5_names_list)
# # # # Print the tuple in reverse order using slicing
# # # print("Your best friends' names in reverse order:")
# # print(" Your Best Five friends names are :")
# # friend_Best5_names_list.reverse()
# # print(friend_Best5_names_list)

#  #### other way round it



# # # # Initialize an empty list to store the names temporarily
# # friend_names_list = []

# # # Ask the user for 5 best friends' names
# # for i in range(7):
# #     name = input(f"Enter the name of your best friend #{i+1}: ")
# #     friend_names_list.append(name)

# # # Convert the list to a tuple
# # friends = tuple(friend_names_list)

# # # Print the tuple in reverse order using slicing
# # print("Your best friends' names in reverse order:")
# # print(friends[::-1])

# #   Task3: Tuple Operations**
# #   create a tuple of 5 Nigerian states entered by the user.
# #   Print the first state and last state.
# #   Check if "Lagos" is in the tuple and print "Yes" or "No".
# #   Print the number of states entered.
#     #(Hint: use the tuple membership)

# # state_1 = input( " Enter first state :")
# # state_2 = input( " Enter first state :")
# # state_3 = input( " Enter first state :")
# # state_4 = input( " Enter first state :")
# # state_5 = input( " Enter first state :")
# # state = ( state_1, state_2, state_3, state_4, state_5)
# # print(f"first state is {state[0]}, and the last state is {state[4]}")
# # print("Kano" in  state)
# # print(" no of state entered is", len(state))

# #      Task4: Tuple Unpacking**
# #      Ask a user for their;

# #First name, Age, Favorite color, Home town, Store them in a tuple profile and unpack into variables.
# #Print and use  escape sequence to align each piece of information nicely.
#       # Data collection steps v#

# first_name = input("Enter your first name: ")
# user_age = input("Enter your age: ")
# favorite_color = input("Enter your favorite color: ")
# home_town = input("Enter your home town: ")
# profile_details = (first_name, user_age, favorite_color, home_town)
# profile_variab = str(profile_details)
# # print and use escape sequence to align each piece of information nicely
# print("\n===== User Profile =====")
# print(f"first_name : \t    | {first_name}")
# print(f" user_age : \t     | {user_age}")
# print(f"favorite_color : \t| {favorite_color}")
# print(f"home_town : \t     | {home_town}")
# print( " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

shop_list1 = input("Enter first item for shopping: \n").title()
shop_list2 = input("Enter second item for shopping: \n").title()
shop_list3 = input("Enter third item for shopping: \n").title()
# converting shop lists input to tuple
tuple_list = (shop_list1, shop_list2, shop_list3)
# coverting tuple to list
shop_list = list(tuple_list)
# Adding more items
print("Enter two more items: ")
shop_list4 = input("Enter fourth item for shopping: \n").title()
shop_list5 = input("Enter fifth item for shopping: \n").title()
shop_list.append(shop_list4)
shop_list.append(shop_list5)
# converting back to tuple
new_shop_list = tuple(shop_list)
# output
print("|".join(new_shop_list))






