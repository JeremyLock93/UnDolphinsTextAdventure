#The Creation of the container class for holding items in a room
# Also on the character's inventory
# Should be able to add, remove, list and transfer items

#Testing with a different approach to the container class

from item import Item

class Container:
    """ This class only handles collections of Items. """
    
    def __init__(self):
        self.contents = {}
        
    def add(self, item):
        self.contents[item.name] = item
        
    def remove(self, item):
        if self.contains(item.name):
            self.contents.remove(item)

    def moveItemTo(self, item, destination):
        
        destination.add(item)
        self.remove(item)
        
    def listContents(self):
        for key in self.contents:
            print(key)
    
    def contains(self, item):
        itemList = list(self.contents.key())
        if item in itemList:
            return True
        else:
            return False

def main():
    """Test Code"""

if __name__ == '__main__':
    main()
