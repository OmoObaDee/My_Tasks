####  Task3: Simulate a football match ticket system #33
#  Store all seat numbers (1 to 50) in a set.
#  Ask users to "book" a seat by entering the number.
#  Remove booked seats from the set.
#  Show remaining seats after each booking.

 ###>>>>>>>>>> seats Storage >>>>>>>>>>>>>
print("Welcome to the Football Match Ticket Booking System!")
print(" Kindly note the Seats available: 1 to 50")
print("Type 'exit' to stop booking.\n")
print(" Continue your Booking please !!!")
seat_number = set(range(1, 51))
print(seat_number)
ticket = int(input( " Select any number from 1 to 50 to book your prefered seat :"))
booked_seat = seat_number
print(F" This are reminding seat Avaialble{booked_seat} The Rest has been booked please")
# Show remaining seats
print("\nRemaining seats:", sorted(seat_number))
print("-*" * 50)

print("\nBooking session ended.")
print(" Thank you for your booking ,see next time.!..!...!")