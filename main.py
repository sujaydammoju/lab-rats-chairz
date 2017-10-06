from room import Room
from flashlight import Flashlight
from character import Enemy

heldItems = []
myHealth = 53
visitedRooms = []

# Set up rooms
kitchen = Room("Kitchen","A dark and dirty room with flies buzzing around.\nThere are dirty beakers, graduated cylinders, and pipettes in the sink.\nThere is a CABINET under the sink.")
kitchen.create_room_item("spoon")
kitchen.create_room_item("fork")
kitchen.create_room_item("spork")
kitchen.create_room_item("rat")
supplyroom = Room("Supply Closet","A small dark room with a musty smell.\nOn one side is a filing CABINET and a large plastic BIN.\nOn the other side is a SHELF full of beakers and a SHOEBOX.")
office = Room("Small Office","A dark room with a mess of books and papers covering the desk.\nYou can READ a book\nYou can look in the DESK")
lab = Room("Laboratory","A bright room with sunlight shining through windows secured by prison bars.\nThere is a SHELF full of beakers on the north wall.")
lab.create_room_item("rat")
locked = Room("locked","")

# Connect rooms
kitchen.link_room(locked, "EAST")
kitchen.link_room(office, "SOUTH")
kitchen.link_room(locked, "WEST")
supplyroom.link_room(office, "EAST")
office.link_room(kitchen, "NORTH")
office.link_room(lab, "EAST")
office.link_room(locked, "SOUTH")
office.link_room(supplyroom, "WEST")
lab.link_room(locked, "SOUTH")
lab.link_room(office, "WEST")
current_room = kitchen

# Set up characters
dave = Enemy("Dmitry", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weaknesses(["FORK","SPORK","KNIFE"])
supplyroom.set_character(dave)

def playerItems():
    # Print out the player's Held Items and let player know if they can USE an item
    if len(heldItems) == 1:
        print("You are holding a "+heldItems[0])
        print("You can DROP "+heldItems[0].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name)
    elif len(heldItems) >= 2:
        print("Your hands are full")
        print("You are holding a "+heldItems[0]+" and a "+heldItems[1])
        print("You can DROP "+heldItems[0].upper()+" or DROP "+heldItems[1].upper())
        if current_room.character is not None:
            print("You can USE "+heldItems[0].upper()+" to fight "+current_room.character.name+" or USE "+heldItems[1].upper())
    return
              

def checkUserInput(current_room,command,heldItems):
    # Convert it to all caps
    command = command.upper()
    
    # All possible user input commands are here
    print("\n")
    if "USE " in command and current_room.get_character() is not None:
        enemyHealth = current_room.character.fight(command[4:])
        if enemyHealth < 1:
            print(current_room.character.name+" is dead")
            current_room.remove_character() # If the enemy is dead, then remove them from the room
    elif "TAKE " in command:
        heldItems = current_room.take_room_item(command[5:],heldItems)
    elif "DROP " in command:
        heldItems = current_room.add_room_item(command[5:],heldItems)
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif current_room.name == "Kitchen" and command == "CABINET" and "flashlight" in heldItems:
        print("You see a KNIFE inside the cabinet.")
        current_room.create_room_item("knife")
    elif current_room.name == "Kitchen" and command == "CABINET":
        print("You check the cabinet, but it's too dark to see if there is anything inside.")
    elif current_room.name == "Small Office" and command == "READ":
        print(u'\u0420\u043e\u0441\u0441\u0438\u044f\u262D'+" You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK" and "key" in heldItems:
        print("There is a BATTERY inside the desk drawer.")
        current_room.create_room_item("battery")
    elif current_room.name == "Small Office" and command == "DESK":
        print("The desk drawer is locked.")
    elif current_room.name == "Laboratory" and command == "SHELF":
        print("The is a small KEY on the shelf.")
        current_room.create_room_item("key")
    else:
        current_room = current_room.move(command) # If it was none of those commands, assume it was a direction.
    return current_room

#THE LOOP
while True:		
    print("\n")
    myHealth = current_room.info(heldItems,myHealth,visitedRooms) # this returns myHealth cuz an enemy in the room could hurt you
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    playerItems()
    command = input("> ")
    current_room = checkUserInput(current_room,command,heldItems)


