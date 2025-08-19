#Task3: Online Store Cart Calculation**

#  Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

#  Start with an empty cart total (cart_total = 0).

# Use assignment operators (+=) to add the price of some items into cart_total.

# Print the list of items and the total price using an f-string like this:
 # Case example

# Creating Cart storage
store_items = ["Book", "Pen", "Bag", "Foodstuffs"]
prices = [500, 100, 2000, 15000]
cart_total = 0
cart_total += prices[0]
cart_total += prices[1]
cart_total += prices[2]
cart_total += prices[3]
print("<>"*15)
print(store_items)
print("<>"*15)
print(prices)
print("<>"*15)
print(f"Total price is #{cart_total}")
print("<>"*15)