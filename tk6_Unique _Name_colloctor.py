#Task2: Unique Name Collector**
# Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

#  >>>>> Collection of Attendees Names In alphabetical Order With no Dulplicate <<<

attendees_Names = set()
 # Input of Names
attendees_Names.add(" Tolulope")
attendees_Names.add(" Olu")
attendees_Names.add(" Segun")
attendees_Names.add(" Bayo")
attendees_Names.add(" Opeyemi")
attendees_Names.add("yetunde")
print(" There is more Attendees available :? Enter Key to Continue")
new_attendee = input(" Input your name :")
attendees_Names.add(new_attendee)
#  >>> Arraiging the Names in an Alphabetical Order
print("\nList of Attendees in Alphabetical Order:")
for person in sorted(attendees_Names):
    print(person)


