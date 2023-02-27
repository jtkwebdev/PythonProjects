#John Kallis
#3/26/2014
#lab section 03, lec lection 01
#jkallis1@umbc.edu
#hw7.py
#this program willl import a text file and change
#alphanumeric characters into their ascii values of a certain base

#fucntion for greeting
def greeting():

    print('This is a filter program that will convert your text file into ASCII values')

#function to check if the file is accessable
def checkfile(file1):

    flag = False
    #try catch to check if the input is an accessable file
    try:
        inputfile = open(str(file1), 'r')
        flag = True
    except:
        flag = False
    return flag

#fuction to check if the base value is between 2 and 9
def checkbase(base1):

    flag = False
    if len(base1) == 1:
        if ord(base1) in range(50,58):
            flag = True
        else:
            flag = False
    else:
        flag = False
    return flag

#fuction to change the alphanumeric characters into ascii values
def changetoascii(file1):

    mylist = []
    inputfile = open(str(file1), 'r')
    for character in inputfile.read():
        if character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            character = int(ord(character))
            mylist.append(character)
        else:
            mylist.append('..')
    return mylist


def basechange(value, base):

    add = value % int(base)
    if value  > 0:
        return str(basechange(value // int(base), base)) + str(add)
    else:
        return str(value)

#loops the basechange function and creates a list
def makelist(value, base):
    
    mylist = []
    for i in range(len(value)):
        if type(value[i]) == type(1):
            mylist.append(basechange(value[i], base))
        else:
            mylist.append(value[i])
    return mylist




#function to create and write the file for output and return the file name
def createfile(filename, changeofbase):
    
    outputfile = open(filename, 'w')
    #loop to add list to the output file 
    for i in range(len(changeofbase)):
        #so the bash starts on a new line
        if i == (len(changeofbase)-1):
            outputfile.write(changeofbase[i] + '\n')
        #adds one to the index so it starts at 1
        elif (int(i) + 1) % 5 != 0:
            outputfile.write(changeofbase[i])
            #adds a space after the first 4 values of each line
            outputfile.write(' ')
        #starts a new line after 5 values are entered
        else:
            outputfile.write(changeofbase[i] + '\n')
    outputfile.close()
    return filename

#main function to bring everything together and name the file
def main():
 
    greeting()
    flag1 = False
    flag2 = False
    while flag1 == False:
        file1 = input('Enter the name of the files: ')
        flag1 = checkfile(file1)
    while flag2 == False:
        base = input('Enter a base between 2 and 9: ')
        flag2 = checkbase(base) 
    asciivalue = changetoascii(file1)
    mylist = makelist(asciivalue, base)
    filename = str(base + '_' + file1)
    print('Done. Use cat to see the file: ', createfile(filename, mylist))
    print(mylist)
main()
