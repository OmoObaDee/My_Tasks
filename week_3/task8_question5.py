#Task5: >>>>>>> Store Inventory Update**
# Create a dictionary called store with items and their available quantities. Example:
# store = {"Book": 10, "Pen": 20, "Bag": 5}
# Ask the user to input the item they want to buy (e.g., "Pen").
# Ask the user to input the quantity they want to purchase.
# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
# Print the updated dictionary in this format:

#  Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
#   After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}

# Solution : Inventory Update
print("."*30)
store = {'semo':20, 'Pencil':25, 'foodstuff': 800, 'trasport':2000}
print("."*30)

# Display the dictionary before purchase
print("Before purchase:", store)
print("."*30)

# Ask the user for the item they want to buy
item = input("Enter any choice of item you want to buy (e.g., 'Pencil'): ")
quantity = int(input("Enter the quantity :"))
print("."*30)
# Update the dictionary using the -= operator
print("."*30)
store[item] -= quantity
# Display the dictionary after purchase
print("."*30)
print("After purchase:", store)
print("."*30)
print(" THANK YOU FOR PARTONAZING US .!!!")

