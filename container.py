class Container():
    # Constructor with optional inOrOn param
    def __init__(self, name, containerArray, inOrOn = None):
        self.name = name
        self.containerArray = containerArray
        self.isOpen = False
        if inOrOn == None:
            self.inOrOn = "in"
        else:
            self.inOrOn = inOrOn

    def open(self):
        result = []
        if not self.isOpen:
            for i in self.containerArray:
                print("You see a "+i.upper()+" "+self.inOrOn+" the "+self.name.lower()+".")
                # Place the interactive item in the room
                result.append(i)
                self.isOpen = True;
        else:
            print("There is nothing else "+self.inOrOn+" the "+self.name.lower()+".")
        return result
