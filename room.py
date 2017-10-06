from random import *

class Room():
    def __init__(self, room_name, room_description):#constructor
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.room_items = list()
        self.character = None

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_character(self, myCharacter):
        self.character = myCharacter

    def get_character(self):
        return self.character

    def remove_character(self):
        self.character = None

    def create_room_item(self,item):
        self.room_items.append(item)

    def add_room_item(self,item,heldItems):
        item = item.lower()
        if heldItems.count(item) > 0:
            self.room_items.append(item)
            heldItems.remove(item)
        elif heldItems.count(item) <= 0:
            print("You can't DROP "+item.upper()+" because you aren't holding that")
        return heldItems

    def take_room_item(self,item,heldItems):
        item = item.lower()
        if len(heldItems) < 2 and self.room_items.count(item) > 0:
            self.room_items.remove(item)
            heldItems.append(item)
            print("You pick up the "+item.upper())
        elif len(heldItems) >= 2:
            print("You can't TAKE "+item.upper()+" because your hands are full")
        elif self.room_items.count(item) <= 0:
            print("You can't TAKE "+item.upper())
        return heldItems

    def get_room_items(self,heldItems):
        for i in self.room_items:
            print("There is a "+i)
            if len(heldItems) < 2:
                print("You can TAKE "+i)

    def info(self,heldItems,myHealth,visitedRooms):
        print("=============")
        print(self.name) # The name of the room
        print("-------------")
        print(self.description) # The description of the room

        #Add to visitedRooms
        if self.name not in visitedRooms:
            visitedRooms.append(self.name)
        
        #Room Items
        for i in self.room_items:
            print("There is a "+i)
            if len(heldItems) < 2:
                print("You can TAKE "+i.upper())

        #Directions
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if room.get_name() in visitedRooms:
                print( "The " + room.get_name() + " is " + direction)
            else:
                print( "There is a door to the " + direction)

        #Characters
        if self.get_character() is not None:
            self.character.describe()
            if self.character.isEnemy():
                myHealth = myHealth - self.character.enemyAttack()
                print("You have "+str(myHealth)+" HP")
        return myHealth

    # Add link_room method
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            if room.get_name() == "locked":
                print("The " + direction + " door is locked.")
                return self
            else:
                return self.linked_rooms[direction]
        else:
            print("Sorry, but you can't " + direction + ".")
            return self
