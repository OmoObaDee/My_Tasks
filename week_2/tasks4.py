# task_1
### Your Favorite Life Quote**
#   Ask the user to input their favorite quote.
#   Convert it to title case.
# #xxxxxxxxx  Print it with quotation marks using escape sequences.xxxxxxxxxx#

# quote = input("Enter your favorite quote: ")
# print(f"\"{quote.title()}\"")
# print(" Thank you for lovely quote !!!")
        #2#
# # task_2**Task 2: Shopping List Manager**
# Create an empty list.
# Ask the user to enter 3 shopping items (one by one).
# Add them to the list.

#  Display the list as a single string, separated by commas.#

# items = []
# itm_1 = input("Enter  first item of your choice: ")
# itm_2 = input("Enter item of your choice: ")
# itm_3 = input("Enter item of your choice: ")
# item_4 = input("Enter the item of your choice :")
# print(" Are done entering your items of your choice:?")
# items.append(itm_1)
# items.append(itm_2)
# items.append(itm_3)
# items.append(item_4)
# res = (",".join(items))
# print(str(res))
# print(" Thank you")

      #3#
# **Task 3: Word Counter**
#  Ask the user for a sentence.
#  Split the sentence into a list of words.
#  Print how many words are in the sentence.

# sen = input("Enter a sentence: ")
# words = sen.split()
# print(len(words))
      #4#
## Task 4: Name Organizer**
# Ask the user to enter 5 names (separated by spaces).
# Convert all names to lowercase.
# Sort the list alphabetically.
# Display them one name per line.
# ******  Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()`
 
# names = input("Enter 5 names of choice and kindly separate by space): ")
# split_names = names.lower().split(" ")
# split_names.sort()
# print(split_names)
# all_names = [print(f"{name}") for name in split_names]
# print(" You have done well...")

     #5#
# # task_5**Task 5: Student Score Tracker**
# Ask the user for 3 student names.
# For each student, ask for their score.
# Store the results in two lists (one for names, one for scores).
# Print a formatted output showing Name — Score, aligned neatly.
#  Tips: You are to start by creating two empty lists.

# name = []
# score = []
# nam = input("Enter name start with Last Name: ")
# nam_1 = input("Enter name Start with Last Name: ")
# nam_2 = input("Enter name starting with the Last Name: ")
# scr = input("Enter score: ")
# scr_1 = input("Enter score: ")
# scr_2 = input("Enter score: ")
# name.append(nam)
# name.append(nam_1)
# name.append(nam_2)
# score.append(scr)
# score.append(scr_1)
# score.append(scr_2)
# print("Name\t| Score")
# print("="*20)
# print(f"{name[0]} \t | {score[0]}")
# print(f"{name[1]} \t | {score[1]}")
# print(f"{name[2]} \t | {score[2]}")

     # 6  #
# Task 6: Word Analyzer**
#  Ask the user to input a word.
#  Print the length of the word.
#  Check if it is all uppercase, all lowercase, or title case.
#  Reverse the word using slicing.

# word = input("Enter a word: ")
# is_upper = word.isupper()
# print(f"the word is in upper case: {is_upper}")
# lower_case = word.islower()
# print(f"the word is in lower case: {lower_case}")
# proper = word.istitle()
# print(f"the word is in lower case: {proper}")
# print(word[::-1])

      ####  7   #####
# Task 7: List Manipulation**
#  Create a list of five cities.
#  Replace the third city with a new one (entered by the user).
#  Remove the last city.
#  Add a new city to the beginning of the list.
#  Print the updated list.

# cities = ["Abeokuta","Oyo","Abuja", "PH", "Oyo",]
# city = input("Enter a city: ")
# cities[2] = city
# cities.pop(-1)
# cities.insert(0,"United Kingdom")
# print(cities)
# print(" THANK YOU FOR YOU TIME .!")









