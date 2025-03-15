import sqlite3
import time
from time import sleep


class roomMate():
    def __init__(self, name, surname, room, gender, age):
        self.name = name
        self.surname = surname
        self.room = room
        self.gender = gender
        self.age = age

    def __str__(self):
        return "Room Mate Info:\nName: {}\nSurname: {}\nGender: {}\nAge: {}\nRoom: {}".format(
            self.name, self.surname, self.gender, self.age, self.room
        )

class roomTable():
    def __init__(self):
        self.connecting()

    def connecting(self):
        self.connection = sqlite3.connect("Dorm.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS RoomMates (Name TEXT, Surname TEXT, Gender TEXT, Age INT, Room INT)")
        self.connection.commit()

    def deconnecting(self):
        self.connection.close()

    def showRoomMates(self):
        self.cursor.execute("SELECT * FROM RoomMates")
        people = self.cursor.fetchall()
        if not people:
            print("There are 0 people in our rooms.")
        else:
            for i in people:
                person = roomMate(i[0], i[1], i[4], i[2], i[3])  # Fix order
                print(person)
                print("\n")

    def roomChanging(self, person_name):
        self.cursor.execute("SELECT * FROM RoomMates WHERE Name = ?", (person_name,))
        person = self.cursor.fetchall()
        try:
            roomNumber = int(input("Which room do you want to move this person to?"))
            self.cursor.execute("Update RoomMates set Room = ? where Room = ?", (roomNumber,person[0][4]))
            sleep(1)
            print("Room has changed successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def roomMateAdding(self, person):
        self.cursor.execute("INSERT INTO RoomMates VALUES (?, ?, ?, ?, ?)",
                            (person.name, person.surname, person.gender, person.age, person.room))
        sleep(1)
        self.connection.commit()
        print("Person added successfully.")

    def roomMateRemoving(self, person):
        self.cursor.execute("DELETE FROM RoomMates WHERE Name = ?", (person,))
        self.connection.commit()
        sleep(1)
        print("Person removed successfully.")
