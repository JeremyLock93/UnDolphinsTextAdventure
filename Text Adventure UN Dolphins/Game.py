
import Player
from rooms import Room

#Create the prompt inside the game loop and provide the commands that will 
# be used from the function of gameloop.

class Game: 
    """
    The main protocol for creating the game loop and other responisbilities
    for which the game class will handle. This way this will handle the main
    functions in which will be created and stored inside. This allows for a 
    smooth set up
    """
    
    def __init__(self):
        """Creates the empty rooms and files for set up"""
        #self.player = player.Player
        self.rooms = {} #The empty dictionary to contain the rooms to be appended too
        #Player object is held in the room (loc)
        self.player = Player
        
        self.isplaying = True
        self.isVerbose = True #This is the way to change verb commands
        
        
    def __str__(self):
        pass
    
    def __repr__(self):
        pass
    
    
        
    def loop(self):
            """ loop(): the main game loop.
            Continues until the user quits. """
            self.isPlaying = True
            while self.isPlaying:
                self.playerAction()
            print("The Game is Over, Thank you for Playing")
            
    def end(self):
        pass
    
    def playerAction(self):
        """Asks for the user input and validation"""
        command = input(">")
        command = command.lower()
        words = command.split() # spliting the white space.
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("Quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        else: # first word is verb
            print("I don't know how to", words[0])
            
    
    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: nothing
        Side effects are the player is able to move through the room
        """
        # Can we go in the chosen direction from here?
        print(direction)
        print(self.here.exits)
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            # newRoomName = self.here.exits[direction]
            exitList = self.here.exits.keys() #Gives the directions for the exits.
            for exits in exitList:
                text = direction
                text += ": " + self.here.exits[exits] #Gives the format of bar: smokey bar
                text += "\n" 
            
            print(text)
            newRoomName = self.here.exits[direction]
            print(self.rooms)
            newRoom     = self.rooms[newRoomName]
            
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
    
    
    def commandGet(self, item):
        """ remove items from the room so that way it can actaully
            be added to the player inventory.
        """
        print("You try to get the", item)

    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player.loc
    
    @here.setter
    def here(self, room):
        self.player.loc = room

def main():
    game = Game()
    game.setup()
    print("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()