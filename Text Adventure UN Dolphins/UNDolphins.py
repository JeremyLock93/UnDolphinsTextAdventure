#Title of the game is UN Dolphins the Posadist Text Adventure or UN Dolphins
# For short so the game file to import the game information for the new game
# Engine.

from Game import Game
from rooms import Room
from Player import player
from item import Item

class Dolphins(Game):
    """This is the subclass of the game engine this is going to be the rendering"""

def setup(self):
    loader = DolphinGameLoader()
    self.rooms = loader.setup



#Staring Location of the game here
    self.here = self.rooms["bar"]
    self.here.describe()




class DolphinGameLoader:
    def setup(self):
        """Setup() creates the rooms for playing"""
        bar = Room ("bar", """
               A large open smokey bar, with several round tables
               and stools. The smell of booze in the air, mixed
               with the scent of cigerette smoke. It was hard to see
               through the crowd of people but to the South,
               the main enterance and exit leads to the hot arid
               Desert Outside.
               """, {"south": "Town Center"})
               
        townCenter = Room ("Town Center", """
                         When going outside, the arid desert is hot and dry,
                         There is not much civilization to the South. To
                         The East there was a small gas station and travel
                         guide of the town. To the West there appears to be 
                         something in the distance, almost as if its was a mirage
                         from your current position it looks as if its a lab?
                                """, {"south": "Wilderness",
                                      "north": "Bar",
                                      "east": "Lab",
                                      "west": "Gas  Station"})
 
                                  
        wilderness = Room ("Wilderness", """
                         When going outside, the arid desert is hot and dry,
                         There is not much civilization to the South. To
                         The East there was a small gas station and travel
                         guide of the town. To the West there appears to be 
                         something in the distance, almost as if its was a mirage
                         from your current position it looks as if its a lab?
                                """, {"north": "Town Center",
                                      "east": "Gas Station",
                                      "west": "Lab"})
                        
        lab = Room ("Lab", """
               High rusty fence with a sign reading
               Restricted Area come at your own risk.
               Some of the fencing was bent over and you could
               easily walk over. Back towards the West is the open wilderness.
               """, {"west": "Town Center",
                     "east": "Wilderness"})
                    
            
    
                                
                                
                                
        self.rooms = {bar.name: bar, 
                townCenter.name:  townCenter,
                wilderness.name:  wilderness,
                lab.name: lab}
        
        return Room

def main():
        Game = Dolphins()
        Game.setup()
        Game.output("Starting Game -- Enter Command.")
        Game.loop()
        Game.End


if __name__ == "__main__":
    main()