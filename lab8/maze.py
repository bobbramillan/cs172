#Mark Boady
#CS 172 - Maze Game
#Drexel University 2018

from room import Room

class Maze:
    #Inputs: Pointers to start room and exit room
    #Sets current to be start room
    def __init__(self, st = None, ex = None):
        # TODO 
        #Room the player starts in
        self.__st = st
        
        #If the player finds this room they win
        # TODO
        self.__ex = ex
        
        #What room is the player currently in
        # TODO
        self.__cur = st
        
    #Return the room the player is in (current)
    def getCurrent(self):
        # TODO
        return self.__cur

    #The next four methods all have the same idea
    #See if there is a room in the direction
    #If the direction is None, then it is impossible to go that way
    #in this case return false
    #If the direction is not None, then it is possible to go this way
    #Update current to the new room (move the player)
    #then return true so the main program knows it worked.
    def moveNorth(self):
        # TODO

        if self.__cur.getNorth() is None:
            print("There is nothing there.")
            return False
        else:
            self.__cur.getNorth() != None
            print("You just went North")
            return True


    def moveSouth(self):
        # TODO
        
        if self.__cur.getSouth() is None:
            print("There is nothing there.")
            return False
        else:
            self.__cur.getSouth() != None
            print("You just went South")
            return True
        
    def moveEast(self):
        # TODO

        if self.__cur.getEast() is None:
            print("There is nothing there.")
            return False
        else:
            self.__cur.getEast() != None
            print("You just went East")
            return True
    
    def moveWest(self):
        # TODO

        if self.__cur.getWest() is None:
            print("There is nothing there.")
            return False
        else:
            self.__cur.getWest() != None
            print("You just went West")
            return True

    #If the current room is the exit,
    #then the player won! return true
    #otherwise return false
    def atExit(self):
        # TODO
        if self.__cur == self.__ex:
            print("You won!")
            return True
        else:
            return False

    #If you get stuck in the maze, you should be able to go
    #back to the start
    #This sets current to be the start room
    def reset(self):
        # TODO
        return self.__cur == self.__st
