#John Kallis
#Maze solving algorithm
#this program takes a .txt file as input
#the file contains a coordinate in each line
#with four values 0 or 1 in the form 0000
#where 0 represents an open path and 1 represents a wall
#the coords. make up a maze.
#this program parses the .txt file and finds the total number 
#of walls for each coordinate. Then recussively traverses the 
#maze with a brute force method, adding walls to paths that do
#not lead to the finish. This is so the completed maze will return
#the path from start to finish with all other paths boxed out.
#(all coordinates will have either 2 or 4 walls)
#I wrote this one for fun. It was an assignment given to a friend 
#which I wrote after "friend" had completed and turned in the assignment
###########
#import sys for sys.exit
#################
import sys
#######################################################
#uses a try catch to check the file input and returns a bool
####################################################
def filecheck(file1):

    try:
        inputfile = open(str(file1), 'r')
        return True
    except:
        return False
##############################################
#loops the file input and returns a valid file name
##############################################
def loopfile():

    flag = False
    while flag == False:
      file1 = input('Enter the name of the text file: ')
      flag = filecheck(file1)
    return file1
#####################################
#creates a 3d list from the .txt input file
#######################################
def createlist(file1):

	mylist=[]
	bigList=[]
	#5x10
	inputFile=open(str(file1),'r')
	for i in inputFile:
		mylist.append(i.strip())
	rowList=[]
	for i in mylist:
		dimList=[]
		for j in i:
			if j!=',':
				j=int(j)
				dimList.append(j)
		dimList.append(0)
		rowList.append(dimList)
		if len(rowList)==10:
			bigList.append(rowList)
			rowList=[]
	return bigList
#######################################
#finds the total number of walls for each coordinate
#######################################
def findTotal(maze): 

	for i in range(len(maze)):
		for j in range(len(maze[i])):
			total=0
			for k in range(4):
				total+=maze[i][j][k]
			maze[i][j][4]=total
	#hard code for the start and end of the maze
	maze[4][9][4]=5
	maze[0][0][4]=-5
	return maze
################################
#loops through the maze and prints it
################################
def printMaze(maze):
	
	for i in range(len(maze)):
		x=''
		for j in range(len(maze[i])):
			x=x+str(maze[i][j])
		print(x)
		print()
#######################################
#recurssivly traverses the maze for open
#paths and prints the coordinate if there
#the coordinate isn't all walls
#######################################
def printSol(maze,row,col,compass):

	if maze[row][col][4]==4:
		return
	else:
		#prints the current coordinate
		print("(",row,",",col,")")
		#starts the maze. moves it down one place
		#moves down as the first move
		#assumed that input will start in upper left
		#corner
		if ((row==0) and (col==0)):
			printSol(maze,row+1,col,2)
		#else:
		#	printSol(maze,row,col+1,1)
		#up and down
		elif ((maze[row][col][0]==0) and (maze[row][col][2]==0)):
			if compass==0:
				printSol(maze, row-1,col,0)
			elif compass==2:
				printSol(maze, row+1,col,2)
		#up and right
		elif ((maze[row][col][0]==0) and (maze[row][col][1]==0)):
			if compass==3:
				printSol(maze,row-1,col,0)
			elif compass==2:
				printSol(maze,row,col+1,1)
		#up and left
		elif ((maze[row][col][0]==0) and (maze[row][col][3]==0)):
			if compass==1:
				printSol(maze,row-1,col,0)
			elif compass==2:
				printSol(maze,row,col-1,3)
		#right and down
		elif ((maze[row][col][1]==0) and (maze[row][col][2]==0)):
			if compass==3:
				printSol(maze,row+1,col,2)
			elif compass==0:
				printSol(maze,row,col+1,1)
		#right and left
		elif ((maze[row][col][1]==0) and (maze[row][col][3]==0)):
			if compass==3:
				printSol(maze,row,col-1,3)
			elif compass==1:
				printSol(maze,row,col+1,1)
		#down and left
		if ((maze[row][col][2]==0) and (maze[row][col][3]==0)):
			if compass==1:
				printSol(maze,row+1,col,2)
			elif compass==0:
				printSol(maze,row,col-1,3)
##############################
#check if row/col are in range
##############################
def checkRowCol(row,col):

	if (row<=4) and (col<=9) and (row>=0) and (col>=0):
		return True
	else:
		return False
##########################################
#uses recursive calls to solve the maze
#maze is the 3d list of maze coordinates
#row and col are the verticies of the list (int, int)
#compass is the direction of traversal	(int)
#i got most of it but didn't feel like finishing 
#########################################
def solveMaze(maze, row, col, compass):

	if checkRowCol(row,col) == True:
		# if the total is negative and the compass is positive
		# that means we are returning the starting position
		# because one of the paths was closed off and a new path begins
		if ((maze[row][col][4]<0) and (compass>0)):
			return maze
		#for everything else
		else:
			#this is the start
			if compass==-5:
				#if there are 2 directions from the starting position
				if ((maze[row][col][0]==0) and (maze[row][col][2]==0)):
					solveMaze(maze, row-1,col,0)
					solveMaze(maze, row+1,col,2)
				#up and right
				#if there are 2 directions from the starting position
				elif ((maze[row][col][0]==0) and (maze[row][col][1]==0)):
					solveMaze(maze,row-1,col,0)
					solveMaze(maze,row,col+1,1)
				#up and left
				#if there are 2 directions from the starting position
				elif ((maze[row][col][0]==0) and (maze[row][col][3]==0)):
					solveMaze(maze,row-1,col,0)
					solveMaze(maze,row,col-1,3)
				#right and down
				#if there are 2 directions from the starting position
				elif ((maze[row][col][1]==0) and (maze[row][col][2]==0)):
					solveMaze(maze,row+1,col,2)
					solveMaze(maze,row,col+1,1)
				#right and left
				#if there are 2 directions from the starting position
				elif ((maze[row][col][1]==0) and (maze[row][col][3]==0)):
					solveMaze(maze,row,col-1,3)
					solveMaze(maze,row,col+1,1)
				#down and left
				#if there are 2 directions from the starting position
				elif ((maze[row][col][2]==0) and (maze[row][col][3]==0)):
					solveMaze(maze,row+1,col,2)
					solveMaze(maze,row,col-1,3)
				#if there is only one path to start
				#go up
				elif maze[row][col][0]==0:
					solveMaze(maze,row-1,col,0)
				#if there is only one path to start
				#go right
				elif maze[row][col][1]==0:
					solveMaze(maze,row,col+1,1)
				#if there is only one path to start
				#go down
				elif maze[row][col][2]==0:
					solveMaze(maze,row+1,col,2)
				#if there is only one path to start
				#go left
				elif maze[row][col][3]==0:
					solveMaze(maze,row,col-1,3)
			#if the position has 3 walls
			elif maze[row][col][4]==3:
				#if up is open
				if maze[row][col][0]==0:
					#close it
					maze[row][col][0]+=1
					#close the wall in the adjacent coord. 
					maze[row-1][col][2]+=1
					#add 1 to the total of both coords.
					maze[row][col][4]+=1
					maze[row-1][col][4]+=1
					#move to the adjacent coord that was just edited
					solveMaze(maze,row-1,col,0)
				#if right is open
				elif maze[row][col][1]==0:
					maze[row][col][1]+=1
					maze[row][col+1][3]+=1
					maze[row][col][4]+=1
					maze[row][col+1][4]+=1
					solveMaze(maze,row,col+1,1)
				#if down is open
				elif maze[row][col][2]==0:
					maze[row][col][2]+=1
					maze[row+1][col][0]+=1
					maze[row][col][4]+=1
					maze[row+1][col][4]+=1
					solveMaze(maze,row+1,col,2)
				#if left is open
				elif maze[row][col][3]==0:
					maze[row][col][3]+=1
					maze[row][col-1][1]+=1
					maze[row][col][4]+=1
					maze[row][col-1][4]+=1
					solveMaze(maze,row,col-1,3)
			#if the position doesnt have 3 walls
			elif maze[row][col][4]!=3:
				#if there are "5"walls you reached the end
				if maze[row][col][4]==5:
					return maze
					sys.exit(0)
				#if it has 4 walls the position is closed
				elif maze[row][col][4]==4:
					return maze
				# if it has 2 walls then travel to the square
				# in the open direction opposite of the direction you came
				elif maze[row][col][4]==2:
					#up and down open
					if ((maze[row][col][0]==0) and (maze[row][col][2]==0)):
						if compass==0:
							solveMaze(maze, row-1,col,0)
						elif compass==2:
							solveMaze(maze, row+1,col,2)
					#up and right
					elif ((maze[row][col][0]==0) and (maze[row][col][1]==0)):
						if compass==3:
							solveMaze(maze,row-1,col,0)
						elif compass==2:
							solveMaze(maze,row,col+1,1)
					#up and left
					elif ((maze[row][col][0]==0) and (maze[row][col][3]==0)):
						if compass==1:
							solveMaze(maze,row-1,col,0)
						elif compass==2:
							solveMaze(maze,row,col-1,3)
					#right and down
					elif ((maze[row][col][1]==0) and (maze[row][col][2]==0)):
						if compass==3:
							solveMaze(maze,row+1,col,2)
						elif compass==0:
							solveMaze(maze,row,col+1,1)
					#right and left
					elif ((maze[row][col][1]==0) and (maze[row][col][3]==0)):
						if compass==3:
							solveMaze(maze,row,col-1,3)
						elif compass==1:
							solveMaze(maze,row,col+1,1)
					#down and left
					elif ((maze[row][col][2]==0) and (maze[row][col][3]==0)):
						if compass==1:
							solveMaze(maze,row+1,col,2)
						elif compass==0:
							solveMaze(maze,row,col-1,3)
				#if there's 1 wall 
				#check where the wall is
				#and travel to the two open positions 
				elif maze[row][col][4]==1:
					#wall on up
					if maze[row][col][0]==1:
						if compass==1:
							#move down and right
							solveMaze(maze,row+1,col,2)
							solveMaze(maze,row,col+1,1)
						elif compass==3:
							#move down and left
							solveMaze(maze,row+1,col,2)
							solveMaze(maze,row,col-1,3)
						elif compass==0:
							#move left and right
							solveMaze(maze,row,col-1,3)
							solveMaze(maze,row,col+1,1)
					#wall on right
					elif maze[row][col][1]==1:
						if compass==1:
							#move down and up
							solveMaze(maze,row+1,col,2)
							solveMaze(maze,row-1,col,0)
						elif compass==2:
							#move down and left
							solveMaze(maze,row+1,col,2)
							solveMaze(maze,row,col-1,3)
						elif compass==0:
							#move left and up
							solveMaze(maze,row,col-1,3)
							solveMaze(maze,row-1,col,0)
					#wall on down
					elif maze[row][col][2]==1:
						if compass==1:
							#move up and right
							solveMaze(maze,row-1,col,0)
							solveMaze(maze,row,col+1,1)
						elif compass==3:
							#move up and left
							solveMaze(maze,row-1,col,0)
							solveMaze(maze,row,col-1,3)
						elif compass==2:
							#move right and left
							solveMaze(maze,row,col+1,1)
							solveMaze(maze,row,col-1,3)
					#wall on left
					elif maze[row][col][3]==1:
						if compass==2:
							#move down and right
							solveMaze(maze,row+1,col,2)
							solveMaze(maze,row,col+1,1)
						elif compass==3:
							#move up and down
							solveMaze(maze,row+1,col,2)
							solveMaze(maze,row-1,col,0)
						elif compass==0:
							#move up and right
							solveMaze(maze,row-1,col,0)
							solveMaze(maze,row,col+1,1)

########################################
#main function to bring it all together
########################################
def main():

    #flags the loop for the run again question 
    masterflag = False
    #gives us the name of a file that exists in the folder
    file1 = loopfile()
    #a 2dlist of the file
    maze = createlist(file1)
    #print the unsolved maze
    printMaze(maze)
    #finds the number of walls for each 
    #coordinate of the maze
    findTotal(maze)
    print()
    #solves the maze
    solveMaze(maze,0,0,-5)
    #prints the path from start to finish
    printSol(maze,0,0,2)
    #printMaze(maze)
    print("you completed the maze!")
    print("good job")
main()
