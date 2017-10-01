from random import *

class Room():
    def __init__(self, room_name, room_description):#constructor
        self.name = room_name
        self.description = room_description
        self.rats = randrange(1,10)
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

    def remove_character(self, Character):
        self.character = None

    def create_room_item(self,item):
        self.room_items.append(item)

    def add_room_item(self,item,heldItems):
        item = item.lower()
        if heldItems.count(item) > 0 and item == "rat":
            self.rats += 1
            heldItems.remove(item)
        elif heldItems.count(item) > 0 and item == "rats":
            self.rats += 1
            heldItems.remove(item)
        elif heldItems.count(item) > 0: #Non-rat item
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
        elif len(heldItems) < 2 and item == "rat":
            heldItems.append("rat")
            self.rats -= 1
        elif len(heldItems) < 2 and item == "rats":
            heldItems.append("rat")
            self.rats -= 1
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

    def info(self,heldItems,myHealth):
        print("=============")
        print(self.name)
        print("-------------")
        print(self.description)
        
        #Rats
        if self.rats == 1:
            print("There is " + str(self.rats) + " rat in this room.")
        else:
            print("There are " + str(self.rats) + " rats in this room.")
        if self.rats > 0 and len(heldItems) < 2:
            print("You can PICK UP A RAT")
        #if heldItems.count("rat") == 1:
#            print("You are holding 1 rat\nYou can SET DOWN A RAT")
#        elif heldItems.count("rat") == 2:
#            print("You are holding 2 rats\nYou can SET DOWN A RAT")
            
        #Room Items
        for i in self.room_items:
            print("There is a "+i)
            if len(heldItems) < 2:
                print("You can TAKE "+i.upper())

        #Held Items
        if len(heldItems) == 1:
            print("You are holding a "+heldItems[0])
            print("You can DROP "+heldItems[0].upper())
        elif len(heldItems) >= 2:
            print("Your hands are full")
            print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
            print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
               
        #Directions
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

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
            return self.linked_rooms[direction]
        else:
            print("Sorry, but you can't " + direction + ".")
            return self
