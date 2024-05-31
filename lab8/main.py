#creates and links room with maze obj
#Bavanan Bramillan bb3323 & william wranovsky wbw32

from maze import Maze
from room import Room



def play(my_maze):
	#Play a game
	while not my_maze.atExit():
		## TODO: Get direction from user
		direction = input("Enter direction (north, south, east, west): ").lower()
		
		## TODO: Based on choice do what was asked.

		if direction == 'north':
			my_maze.moveNorth()
		elif direction == 'south':
			my_maze.moveSouth()
		elif direction == 'east':
			my_maze.moveEast()
		elif direction == 'west':
			my_maze.moveWest()
		else:
			print("Direction invalid, try again.")

	

# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters. 
## TODO: Create the SIMPLE_MAZE

Room1 = Room("Room 1")
Room2 = Room("Room 2")
Room3 = Room("The exit room")

Room1.setEast(Room2)
Room2.setNorth(Room3)
Room1.setEast(Room1)
Room2.setNorth(Room2)




Room1.setWest(Room2)
Room2.setEast(Room1)
Room2.setWest(Room3)
Room3.setEast(Room2)
Room2.setNorth(Room3)

SIMPLE_MAZE = Maze(Room1, Room2)


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded. 
## TODO: Create the INTERMEDIATE_MAZE
INTERMEDIATE_MAZE =  Maze(Room2, Room3)

if __name__=="__main__":
	play(INTERMEDIATE_MAZE)

