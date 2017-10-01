from room import Room
from flashlight import Flashlight
from character import Enemy

heldItems = []
myHealth = 53

# Set up rooms
kitchen = Room("Kitchen","A dark and dirty room with flies buzzing around.\nThere are dirty beakers, graduated cylinders, and pipettes in the sink.\nThere is a CABINET under the sink.")
kitchen.create_room_item("spoon")
kitchen.create_room_item("fork")
kitchen.create_room_item("spork")
supplyroom = Room("Supply Closet","A small dark room with a musty smell.\nOn one side is a filing cabinet and a large plastic bin.\nOn the other side is a shelf full of beakers and a shoebox.")
office = Room("Small Office","A dark room with a mess of books and papers covering the desk.\nYou can READ a book\nYou can look in the DESK")
lab = Room("Laboratory","A bright room with sunlight shining through windows secured by prison bars.")

# Connect rooms
kitchen.link_room(office, "SOUTH")
supplyroom.link_room(office, "EAST")
office.link_room(lab, "EAST")
office.link_room(supplyroom, "WEST")
office.link_room(kitchen, "NORTH")
lab.link_room(office, "WEST")
current_room = kitchen

# Set up characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
supplyroom.set_character(dave)


def checkUserInput(current_room,command,heldItems):
    #Convert it to all caps
    command = command.upper()
    
    #Check user input
    print("\n")
    if "TAKE " in command:
        heldItems = current_room.take_room_item(command[5:],heldItems)
    elif "DROP " in command:
        heldItems = current_room.add_room_item(command[5:],heldItems)
    elif "TALK" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif "FIGHT" in command and current_room.get_character() is not None:
        current_room.character.talk()
    elif current_room.name == "Small Office" and command == "READ":
        print(u'\u0420\u043e\u0441\u0441\u0438\u044f\u262D'+" You can't read it. It's written is some strange Cyrillic script.")
    elif current_room.name == "Small Office" and command == "DESK":
        print("There is a battery inside.")
        current_room.batteries += 1
    elif current_room.name == "Small Office" and command == "DESK" and holdingKey < 1:
        print("The desk drawer is locked.")
    elif command == "PICK UP A RAT" and current_room.rats > 0 and len(heldItems) < 2:
        heldItems.append("rat")
        current_room.rats -= 1

    #elif command == "SET DOWN A RAT" and heldItems.count("rat") > 0:
        #heldItems.remove("rat")
        #current_room.rats += 1
    else:
        current_room = current_room.move(command)
    return current_room

#THE LOOP
while True:		
    print("\n")
    myHealth = current_room.info(heldItems,myHealth)
    if myHealth <= 0:
        print("You died.\nGAME OVER")
        break
    command = input("> ")
    current_room = checkUserInput(current_room,command,heldItems)


