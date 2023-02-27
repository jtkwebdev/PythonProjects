#John Kallis
#4/1/2014
#jkallis1@umbc.edu
#homework 7
#section 01 lab 03
#this program will convert the characters of a text file into a given base change of the 
#ascii values. 

#a function for the greeting
def greeting():

    print('This is a filter program that will convert your text file into ascii values')

#trys to open the file to see if it exists using a try catch
def checkfile(file1):
    flag = False
    try:
        inputfile = open(str(file1), 'r')
        flag = True
    except:
        flag = False
    return flag

#checks if the input is 2-9
def checkbase(base):

    flag = False
    if len(base) == 1:
        if base in '23456789':
            flag = True
        else:
            flag = False
    else:
        flag = False
    return flag

#changes the characters of the .txt file into an ascii value in a list
def changetoascii(file1):

    mylist = []
    inputfile = open(str(file1), 'r')
    for i in inputfile.read():
        if i in 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            i = int(ord(i))
            mylist.append(i)
        else:
            mylist.append(str(".."))
    return mylist

#changes the ascii values into the inputed base using recursion
def basechange(value, base):
    
    add = value % int(base)
    if value == 0:
        changedbase = str(value)
        #I couldn't figure out how to get the correct calculation so I found a work around
        return changedbase[1:]
    else:
        return  str(basechange(value // int(base), base)) + str(add)
 
#loops the recursive function for all of the objects in the list
def makealist(asciivalue, base):

    mylist = []
    for i in range(len(asciivalue)):
        if type(asciivalue[i]) == type(1):
            mylist.append(basechange(asciivalue[i], base))
        else:
            mylist.append(asciivalue[i])
    return mylist

#outputs the file with the base change
def createfile(filename, mylist):

    outputfile = open(filename, 'w')
    for i in range(len(mylist)):
        if i == (len(mylist)-1):
            outputfile.write(mylist[i] + '\n')
        elif (int(i) + 1) % 5 != 0:
            outputfile.write(mylist[i])
            outputfile.write(' ')
        else:
            outputfile.write(mylist[i] + '\n')
    outputfile.close()
    return filename

#breings it all together
def main():

    greeting()
    flag1 = False
    flag2 = False
    while flag1 == False:
        file1 = input('Enter the name of the file: ')
        flag1 = checkfile(file1)
    while flag2 == False:
        base = input('Enter a base between 2 and 9: ')
        flag2 = checkbase(base)
    asciivalue = changetoascii(file1)
    mylist = makealist(asciivalue, base)
    filename = str(base + '_' + file1)
    print('Done. Use cat to see the file: ', createfile(filename, mylist))

main()
