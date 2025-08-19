###   TUPLE- A tuple is an ordered, immutable (unchangeable) collection of items in Python.###S  #####

## Creating Parentheses()
#  xxxxxxx  Example 1   #####

# fruits = ("apple", "banana", "cherry")
# print(fruits)  
# # output : ('apple', 'banana', 'cherry')

  # 2#
# # Without parentheses(tuple packing)
# number = 1, 2, 3
# print(number)
# # # output : (1,2,3)
# numbers = input(" enter any number of choice sepetared with coma :")
# print(numbers)
# print(" Thank you")

#.3
# #  Single-item tuple (must include a comma)
# single_item = ("Mango", "Maize")
# print(single_item)      
#  # Output ('apple',)
# print(type(single_item)) 
# # # output<class 'tuple'>
# single_item = ("Mango",)
# print(single_item)      
#  # Output ('apple',)

# print(type(single_item)) 
# # output<class 'tuple'>


# ##    4. Using the tuple() constructor   #

# fruits_list = ["apple", "banana", "cherry", "Maize"]
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)  
# # Output : ('apple', 'banana', 'cherry', 'Maize')

#      Characteristics of Tuples #  
# 1. Ordered – Items have a fixed position.

# 2. Immutable – Cannot change after creation.

# 3. Allow duplicates – Same value can appear multiple times.

# 4. Can contain mixed data types – Strings, integers, lists, etc.

# 5. Can be nested – Tuples inside tuples.


    #  ORDERED  ###

# colors = ("red", "green", "blue", " White")
# print(colors[0])  
# # Output : red  
 
# colors = ("red", "green", "blue", " White")
# print(colors[1]) 
# # Output: green

###  # Immutable ( uncomment and run. This will cause an error)

#colors[1] = "Red"  
#  TypeError

# # Allow duplicates
# numbers = (1, 2, 2, 3,4,4,4,4)
# print(numbers)  
# # Output : (1, 2, 2, 3, 4, 4, 4, 4)

# numbers = (" ayo", "Ayo","Ayo", "Ayo")
# print(numbers)
# print("Thank you")

# Mixed data types #3
# mixed = ("apple", 3, 8, "Apple", False, "Ayo",True, 5.6)
# print(mixed)  
# # Output :  ('apple', 3, 8, 'Apple', False, 'Ayo', True, 5.6)

# # Nested tuples
# nested = (("a", "b"), (1, 2),(2, 2), ("Oluayo"), ("c," "d"))
# print(nested)  
# #  Output : (('a', 'b'), (1, 2), (2, 2), 'Oluayo', 'c,d')


#   Tuple Operations #
#  Even though tuples are immutable, you can still perform several operations

# 1. Indexing

# fruits = ("apple", "banana", "cherry")
# print(fruits[2])   
# # output : cherry

# # print(fruits[-1])  
# # # output : cherry

# # 2. Slicing

# print(fruits[0:2])  
# # output : ('apple', 'banana')
# print(fruits[0:1])
# # output: ('apple', 'banana')

# print(fruits[::-1])  
# Output :('cherry', 'banana', 'apple')

# 3. Concatenation
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# tuple3 = (5, 9)
# tuple4= (5, 7)
# result = tuple1 + tuple2 +tuple3 +tuple4
# print(result)  
# # output :(1, 2, 3, 4, 5, 9, 5, 7)

# # 4. Repetition
# nums = (1, 2, 4, 5)
# print(nums * 3)  
# # Output :  (1, 2, 4, 5, 1, 2, 4, 5, 1, 2, 4, 5)

# nums = (1, 2, 4, 5)
# print(nums * 4) 
# # output : (1, 2, 4, 5, 1, 2, 4, 5, 1, 2, 4, 5, 1, 2, 4, 5)

# # 5. Membership

# fruits = ("apple", "banana", "cherry")
# print("banana" in fruits)  
# # output : True
# print("grape" not in fruits) 
#  # output : True

# fruits = ("apple", "banana", "cherry")
# print("Orange" in fruits) 
# # output : False

# fruits = ("apple", "banana", "cherry")
# print("banana" not in fruits)  
# #output : False

# # 6. Iteration
# for fruit in fruits: 
#     print(fruit)

      #Working with Tuples**
#  You can’t modify a tuple directly, but you can
#  Convert it to a list, modify it, then convert back.
#  Use built-in functions to work with tuple contents.

# 1. Unpacking Tuples
# person = ("John", 40, "Nigeria",)
# name, age, country = person
# print(name)     
# print(age)     
# print(country)  
# print("Thank you")

#Tuple Methods**
#Tuples have only two methods.

# dont count() and dot index()

# numbers = (1, 2, 2, 3, 4)

# # print(numbers.count(2))  
# # # 2  (counts occurrences of 2)

# print(numbers.index(1)) 
#  # 0 (position of first occurrence of 3)

#Converting Between List and Tuple

# # Tuple to List
# t = (1, 2, 3)
# lst = list(t)
# lst.append(4)
# print(lst) 
#  #  output : [1, 2, 3, 4] # append(4) means to add 4 to the list

# # List back to Tuple
# t = tuple(lst)
# print(t)  
# # (1, 2, 3, 4)


#   # QUESTION TO BE ASKED  #
person = ("John", 40, "Nigeria", "location")
name, age, country, Abeokuta = person
print(Abeokuta)
print(name)     
print(age)     
print(country)  
print("Thank you")

# # ## Built-in Functions with Tuples #
# nums = (4, 1, 7, 3)
# # print(len(nums))   
# # # 4
# # print(max(nums))
# # # 7
# # print(min(nums))   
# # # 1
# print(sum(nums))   
# # # 15

