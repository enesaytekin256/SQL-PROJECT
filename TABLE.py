from time import sleep

from ROOM import *

print("""
****************************************

WELCOME TO ROOM CONTROL PANEL

THERE IS THE FUNCTION LIST OF THIS PANEL

1. SHOW ROOM MATES
2. ADD ROOM MATE
3. REMOVE ROOM MATE
4. CHANGE ROOM
5. PRESS 'q' TO QUIT 

****************************************
""")

room = roomTable()


while True:
    choice = input("Which function you want to use?\n")
    if (choice == "q"):
        print("QUITTING THE PANEL...")
        break
    elif (choice == "1"):
        room.showRoomMates()
    elif (choice == "2"):
        name = input("Name : ")
        surname = input("Surname : ")
        gender = input("Gender : ")
        age = input("Age : ")
        room_number = input("Room Number : ")

        new_person = roomMate(name, surname, room_number, gender, age)

        room.roomMateAdding(new_person)
    elif (choice == "3"):
        removedPerson = input("WHICH PERSON YOU WANT TO REMOVE?")
        room.roomMateRemoving(removedPerson)
    elif (choice == "4"):
        changedRoom = input("WHICH PERSON YOU WANT TO CHANGE ROOM?")
        room.roomChanging(changedRoom)
    else:
        print("WRONG INPUT...")
