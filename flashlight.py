class Flashlight():
    #constructor - requires size, color, and int charge as params
    def __init__(self,size,color,charge):#constructor
        self.size = size #small or large
        self.color = color
        self.charge = charge #int from 0 to 100
        self.batteries = 2
        self.bulb = 1
        self.turnedOn = false

    #getter that returns the amount of charge in the flashlight
    

    #setter that removes 1 battery if there are batteries in the flashlight
    #returns 1 if successful, to add 1 battery to room
    def remove_batteries(self):
        if self.batteries > 0:
            self.batteries -= 1
            print("You remove 1 battery.")
            return 1 #add 1 battery to room
        else:
            print("There aren't any batteries in the flashlight.")
            return 0

    #setter that removes the bulb if there is a bulb in the flashlight
    #returns 1 if successful, to add 1 bulb to room
    def remove_bulb(self):
        if self.bulb > 0:
            self.bulb -= 1
            print("You remove the flashlight bulb.")
            return 1 #add 1 bulb to room
        else:
            print("There isn't a bulb in the flashlight.")
            return 0

    #setter that adds 1 battery if there are batteries in the room and space in the flashlight
    #returns -1 if successful, to remove 1 battery from room
    def add_batteries(self,roomBatteries):
        if self.batteries < 2 and roomBatteries > 0:
            self.batteries += 1
            print("You put 1 battery in the flashlight.")
            return -1 #-1 battery in the room
        elif self.batteries < 2 and roomBatteries <= 0:
            print("There are no batteries in the room.")
            return 0
        elif self.batteries >= 2 and roomBatteries > 0:
            self.batteries = 2
            print("The flashlight already has enough batteries.")
            return 0

    #setter that adds 1 bulb if there are bulbs in the room and space in the flashlight
    #returns -1 if successful, to remove 1 bulb from room
    def add_bulb(self,roomBulbs):
        if self.bulb <= 0 and roomBulbs > 0:
            self.bulb = 1
            print("You remove the flashlight bulb.")
            return -1 #-1 bulb in the room
        elif self.batteries < 2 and roomBulbs <= 0:
            print("There are no flashlight bulbs in the room.")
            return 0
        else:
            print("There is already a bulb in the flashlight.")
            return 0           

    #setter that turns the flashlight on
    def turn_on(self):
        if not self.turnedOn:
            if self.batteries == 2 and self.bulb == 1:
                self.turnedOn = true
                print("You turn the flashlight on.")
            else:
                print("It won't turn on.")

    #setter that turns the flashlight off
    def turn_off(self):
        if self.turnedOn:
            self.turnedOn = false
            print("You turn the flashlight off.")
            
