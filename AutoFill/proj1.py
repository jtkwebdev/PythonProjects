#John Kallis
#4/7/2014
#project 1
#sec 01 lab sec 03
#jkallis1@umbc.edu
#the program will floodfill a text file of Is and -s with @s
#proj1.py


#uses a try catch to check the file input and returns a bool
def filecheck(file1):

    try:
        inputfile = open(str(file1), 'r')
        return True
    except:
        return False

#loops the file input and returns a valid file name
def loopfile():

    flag = False
    while flag == False:
      file1 = input('Enter the name of the text file: ')
      flag = filecheck(file1)
    return file1


#checks if the file is rectangular from a 2Dlist, returns a bool
def checkrectangle(mylist):

    flag = True
    for i in range(len(mylist)):
        if len(mylist[i]) != len(mylist[0]):
            flag = False

    if flag == False:
        print('file is not a rectangle')
    return flag

#checks for characters other then _ and I in the 2dlist, returns a bool
def checkcharacters(mylist):

    flag = True
    if len(mylist) > 0:
        for i in mylist:
            for j in i:
                if j not in '-I':
                    flag = False
                if flag == False:
                    return print('contains characters other then - and I')
    return flag


#creates a list from the file
def createlist2(file1):

    mylist = []
    mylist3 = []
    inputfile = open(str(file1), 'r')
    for i in inputfile:
        mylist.append(i.strip())
    inputfile.close()
    for i in mylist:
        mylist2 =[]
        for j in i:
        	if j == ',':
                    pass
        	else:
                    mylist2.append(j)
        mylist3.append(mylist2)
    return mylist3

#checks the row input and column input and returns true or false
def rowcheck(row, column, mylist):

    flag = False
    #try catch for the row input
    try:
        row = int(row)
        #if input is an int, checks if its in range of 2dlist
        if row in range(len(mylist)):
            flag = True
    except:
        return False
    #if row input is an int checks for valid column input
    try:
        column = int(column)
        if flag == True:
            #checks for column in range (we know the file
            #is rectangluar already so any row will do)
            if column in range(len(mylist[row])):
                return True
    except:
        return False
    #returns false if row is in range and column is int but not in range
    return False

#prints the grid with spaces as a string from the 2dlist
def printlist(mylist):

    for i in mylist:
        string = ''
        for j in i:
            string += j+' '
        print(string)

#checks for correct input from stepbystep/runagain and returns a bool
def checkforyesorno(yesorno):


    if (yesorno.lower() == 'yes') or (yesorno.lower() == 'no'):
        return True
    else:
        return False


#does all the replacements using recurssion
#inputs: mylist, row, col, stepbystep
#outputs mylist with @ replacements
def fillwithat(grid, therow, thecol, display):


    if rowcheck(therow, thecol, grid) == True:
        if grid[therow][thecol] != '-':
            return grid  
        #changes - to @
        grid[therow][thecol] = '@'
        #prints the step by step if requested
        if display == 'yes':
            printlist(grid) 
            print()
        #does the calculations for the fill
        fillwithat(grid, therow - 1, thecol, display)
        fillwithat(grid, therow, thecol - 1, display)
        fillwithat(grid, therow, thecol + 1,display)   
        fillwithat(grid, therow + 1, thecol, display)
    return grid
 

def main():


    #flags the loop for the run again question 
    masterflag = False
    #gives us the name of a file that exists in the folder
    file1 = loopfile()
    #a 2dlist of the file
    mylist = createlist2(file1)
    #flags to check the requiremnts of the file
    character = checkcharacters(mylist)
    rectangle = checkrectangle(mylist)
    
    if (character == True) and (rectangle == True):
      print('valid input..........will process')
      printlist(mylist)
      while masterflag == False:
        flag1 = False
        flag2 = False
        flag3 = False
        #loops for correct row and col inputs
        while flag1 == False:
            row = input('enter a row: ')
            column = input('enter a column: ')
            flag1 = rowcheck(row, column, mylist)
        #changes input variables to ints after it runs through a try catch in the rowcehck function
        row = int(row)
        column = int(column)
        #loops the stepbystep question for yes or no to be used in the fillwithat function
        while flag2 == False:  
            stepbystep = input('print out step by step?    enter yes: ')
            flag2 = checkforyesorno(stepbystep)
        
        mylist = fillwithat(mylist, row, column, stepbystep)
        print('***THIS IS WHAT IT LOOKS LIKE AFTER PROCESSING YOUR ROW AND COL****')
        #displays the grid filled with @s
        printlist(mylist)
        while flag3 == False:
            runagain = input('Go again?   Enter Yes: ')
            flag3 = checkforyesorno(runagain)
            if runagain.lower() == 'no':
                masterflag = True

                
main()

