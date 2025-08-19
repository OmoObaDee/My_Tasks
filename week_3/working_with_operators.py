#  WORKING WITH PYTHON OPERATORS
#- Operators are special symbols in Python that perform operations on variables and values.

#   Here we will focus on:

# 1. Comparison Operators

# 2. Assignment Operators

# 3. Logical Operators

# NOW LET TALK ABOUT COMPARISION OPERATORS

# >>>>> Comparison operators are used to compare two values. The result is always `True` or `False`.

#| Operator | Example  | Meaning                  |
#| -------- | -------- | ------------------------ |
#| `==`     | `5 == 5` | Equal to                 |
#| `!=`     | `5 != 3` | Not equal to             |
#| `>`      | `7 > 4`  | Greater than             |
#| `<`      | `3 < 8`  | Less than                |
#| `>=`     | `6 >= 6` | Greater than or equal to |
#| `<=`     | `2 <= 5` | Less than or equal to    |

# EXAMPLES :
a=10
b=20
c=30
d=40

# print(a==b,a==c,c==d) # Equal To
# # Output :False False False

# print(a !=b, c !=d, d!=a) # Not equal to
# # output : True True True

# print(a>b>c>d, a>d, d>c,c>c) # Greater than
# #output : False False True False

# print(a<b,b<d,c<d,c<b,b<b) # Less Than
# #output: True True True False False

# print(a>=10, b>=20, c>=10, d>=40) # Greaster than
# # output: True True True True

# print(b<=25,a<=25,c<=25,d<=25) # Less than and equal to
# # output: True True False False


# Use case Example- Student Exam Result

# score = 75

# print(score >= 50)  # True (Passed)
# # output: True
# print(score < 50)   # False (Failed)
# #output: False
# print(score == 100) # False (Not full marks)
# #output: False
# print(score <=101) # True( Passed)


#    NOW>>>>>>>> Assignment Operators <<<<<<<<<<<<<
#   Assignment operators are used to assign values to variables. 
#   They can also combine an operation with assignment, so instead of writing `x = x + 5`, we can write x` += 5`.

#| Operator | Example   | Meaning                        |
# -------- | --------- | ------------------------------- |
# `=`      | `x = 10`  | Assigns value 10 to `x`         |
# `+=`     | `x += 5`  | Adds 5 to `x` (`x = x + 5`)     |
# `-=`     | `x -= 3`  | Subtracts 3 from `x`            |
# `*=`     | `x *= 2`  | Multiplies `x` by 2             |
# `/=`     | `x /= 4`  | Divides `x` by 4                |
# `%=`     | `x %= 3`  | Stores remainder after division |
# `**=`    | `x **= 2` | Raises `x` to the power of 2    |
# `//=`    | `x //= 2` | Floor divides `x` by 2          |


x = 10
# print("Initial value:", x)
# # output: Initial value: 10

# x += 5
# print("After x += 5:", x)
# # Output :After x += 5: 15

# x -= 2
# print("After x -= 2:", x)
# output: After x -= 2: 8

# x *= 3
# print("After x *= 3:", x)
# #output: After x *= 3: 30

# x /= 4
# print("After x /= 4:", x)
# #output: After x /= 4: 2.5

# # x %= 3
# # print("After x %= 3:", x)
# # # output: After x %= 3: 1

# x = 4
# x **= 2
# # print("After x **= 2:", x)
# # # output : After x **= 2: 16

# x //= 3
# print("After x //= 3:", x)
# # output: After x //= 3: 5 meaning 16/3=5 remainder 1 but we only need 5


# Use case Example:

# Define variables
balance = 1000
deposit = 200
withdraw = 150


balance += deposit   # Add deposit
balance -= withdraw  # Subtract withdrawal

print("Updated Balance:", balance)  
# Output: Updated Balance: 1050
print(" All Details of the Account :", deposit, withdraw)
print(" Thank You !!!")


#   Logical Operators # 

# Logical operators are used to combine conditional statements. 
# They work with Boolean values (True or False).

#| Operator | Example            | Meaning                                |
#| -------- | ------------------ | -------------------------------------- |
#| `and`    | `x > 5 and x < 15` | True if both conditions are true       |
#| `or`     | `x < 5 or x > 20`  | True if at least one condition is true |
#| `not`    | `not(x == 10)`     | True if the condition is false         |

x = 10
y = 20

# and operator
# print(x > 5 and y > 15)  # True

# # or operator
# print(x < 5 or y > 15)   # True

# # not operator
# print(not(x==10))  # false


# Use case example1 - Scholarship Eligibility

#Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)  
# Output: Scholarship Eligible: True

# Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)  
# Output: Access Granted: True (because age < 25 even without ticket)