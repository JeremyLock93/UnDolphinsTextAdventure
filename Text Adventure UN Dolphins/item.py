#This is the item class for creating items.

class Item:
    """
    Items are found in rooms, or in the player inventory.
    (Possibly we'll change that to being found in Container objects?)
     
    They may be used to solve puzzles, give points to score, etc.
    """
     
    def __init__(self, name, description):
         self.name = name
         self.description = description
         
    def __str__(self):
        return self.name + " : " + self.description