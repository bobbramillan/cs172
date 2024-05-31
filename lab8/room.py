#Simple Maze Class
#Mark Boady
#Drexel University
#CS 172

class Room:
    #Constructor sets the description
    #And all four doors should be initially set to None
    def __init__(self, descr):
        # TODO
        self.__descr = ""
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
        
    #Accessors
    #Return the correct values
    def __str__(self):
        # TODO: 
        return self.__descr
    
    def getNorth(self):
        # TODO: 
        return self.__north
    
    def getSouth(self):
        # TODO: 
        return self.__south
    
    def getEast(self):
        # TODO: 
        return self.__east
    
    def getWest(self):
        # TODO: 
        return self.__west
        
    #Mutators
    #Update the values
    def setDescription(self, d):
        # TODO: 
        self.__descr = d
    
    def setNorth(self, n):
        # TODO: 
        self.__north = n
    
    def setSouth(self, s):
        # TODO: 
        self.__south = s
    
    def setEast(self, e):
        # TODO: 
        self.__east = e
    
    def setWest(self, w):
        # TODO: 
        self.__west = w
    