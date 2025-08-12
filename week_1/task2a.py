#Using on the topic taught to list the information below####
# Ask for  for their first name and age and print a welcoime message usinmg an f-string
# name = "oludayo"
# age= 47
# print(f" Welcome{name}," " \t\t {age} years old")
# print(" Are you done entering your detail?")
# print(" Thank you for detail")

# ## Price Display with Type casting ####
# pricestr = input("How much is garri per paint?(in Naira):")
# #convert to string to float#
# price = float(pricestr)
# print("Thank you for your time")

# #Get Naira part (Whole Number)
# naira = int (110)
# print(naira)

# #p# Get Kobo Part( Fraction part 1100 rounded 
# kobo = (round((price-naira)* 100))
# print(kobo)

# ##Displ;ay the Amount in Niara and Kobo
# print(F"The price of garri is (naira)naira and (kobo)kobo")

# details of student
# eba

#ASK FOR INPUT
# market_name = input(" Enter the market_name:")
# num_traders =int(input("traders number :"))
# daily_revenue = float(input("Enter the daily revenue in naira :"))
# print(f"{market_name } \n {num_traders } \n { daily_revenue}")

# #display the result using F-string
# print(F" market_name : (market_name+)")
# print(F" Number of Traders : (num_traders:)")
# print(f" daily revenue: $(daily_revenue:,2F)")

# get input
# customers_name = input("Enter customer Full name :")
# units_consumed = int(input("Enter units consumed (kw/h):"))
# cost_per_unit = float(input(" enter cost per Units :"))
# print(f"{ customers_name} \n{"unit_consumed"} ln{ cost_per_unit}")
# # calculate ther total
# total_bill = units_consumed * cost_per_unit

# ### print formatted receiept

# print(" \n electricity Bill Receipt")
# print("  xxxxxxxxxxxxxxxxxxxxxxxx")
# print(F" Customers Name : {customers_name}")
# print(f" Customer Consumed {units_consumed}")
# print(f" cost per unit : {cost_per_unit:2f}")
# print(" xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# print(" \n\t\t Thank you for your time")

### mixing  data tyoe
# ask for school fees breakdown
school_name =input(" Enter your school name :")
Tuition_fee = input( "enter Amout :")
Hostel_fees = input(" Enter the Amount of your hostel fees :")
feeding_fess =input(" Enter the total amount of your feeding :")
print(F"{school_name} \n {Tuition_fee} \n {Hostel_fees} \n {feeding_fess}")