#John Kallis
#4/1/2014
#hw8.py
#jkallis1@umbc.edu
#sec 01 lab sec 03
#this program is a game for two players to guess a word

#checks if file exisits
def checkfile(file1):

    try:
        inputfile = open(str(file1), 'r')
        return True
    except:
        return False

#loops for the input of the file
def loopfile():

    flag = False
    while flag == False:
        file1 = input('Enter the name of your word file: ')
        flag = checkfile(file1)
        if flag == False:
            print('no such file exists')  
        else:
            return file1
        
#returns a list of all of the lines in the text file
def rounds(file1):

    inputfile = open(str(file1), 'r')
    mylist1 = []
    for currentline in inputfile:
        mylist1.append(currentline.strip())
    inputfile.close()
    return mylist1

#creats the blanks for the word
def blanks(therounds):

    mylist = []
    for i in therounds:
        mylist.append('_ ')
    return mylist

#creates a list for the answer
def theanswer(theround):

    mylist2 = []
    theround = theround.upper()
    for i in theround:
        mylist2.append(i)
    return mylist2

#checks for the correct input for the letter
def lettercatch(letter):
    letter = letter.upper()
    if len(letter) == 1:
        if ord(letter) in range(65,91):
            return True
        else:
            return False
    else:
        return False

#loops the letter input
def letter():

    flag = False
    while flag == False:
        letter = input('enter a letter: ')
        letter = letter.upper()
        flag = lettercatch(letter)
    return letter

#prints the score board
def score(score1, score2, turn):
    
    print()
    if turn == 0:
        print("Player 1's turn")
    else:
        print("Player 2's turn")

    print('----------')
    print('player 1 score: ', score1)
    print('player 2 score: ' ,  score2)
    print('----------')
    print()

#displays the final scoreboard
def thefinal(score1, score2):
    
    print()
    print('THE FINAL SCORE IS: ')
    print( '----------')
    print('player 1 score: ', score1)
    print('player 2 score: ' ,  score2)
    print('----------')
    print()
    if score1 == score2:
        print('The game is a draw')
    if score1 > score2:
        print('player 1 WINS')
    if score1 < score2:
        print('player 2 WINS')

#main function uses while and for loops and counts to run the game
def main():
    #empty variable for score
    score1 = 0
    score2 = 0
    #count for whose turn it is
    player = 0
    #for the text file input
    file1 = loopfile()
    #the length of this list gives us the number of rounds
    theround = rounds(file1)
    #loops for each round
    for i in range(len(theround)):
        print('Round', i+1)
        #empty lists for the letters already inputed
        usedletters = []
        usedletters2 = []
        #takes a list of the word for the round and turns it into a string
        board = blanks(theround[i])
        answer = theanswer(theround[i])
        board2 = ' '.join(e for e in board)
        #continues to loop until all of the blanks are gone
        while '_' in board2:
            #gives us the turn number using 0 or 1
            turn = player % 2
            print()
            #displays the board
            print(board2)
            #displays the score
            score(score1, score2, turn)
            #makes the letter uppercase and loops input
            letter1 = letter()
            print()
            #subtracts points if the letter was already inputed this round
            if (letter1 in usedletters) or (letter1 in usedletters2):
                print('the letter ' + letter1 + ' has already been selected')
                if turn == 0:
                    score1 -= 1
                else:
                    score2 -= 1
                player += 1
            #for if the letter hasnt been used but is not in the answer
            elif (letter1 not in answer):
                print('no letter ', letter1, ' in the word')
                usedletters.append(letter1)
                player += 1
            #loops through the answer and replaces blanks with the correct
            #letter if the letter hasnt been entered and awards points
            if (letter1 not in usedletters) and (letter1 not in usedletters2):
                for j in range(len(answer)):
                    if letter1 == answer[j]:
                        board[j] = answer[j]
                        board2 = ' '.join(e for e in board)
                        if turn == 0:
                            score1 += 1
                        else:
                            score2 += 1    
            #if the letter is in the answer it is added to a list
            if (letter1 in answer):
                usedletters2.append(letter1)        
        #displays the score until all of the blanks are gone
        if '_' in board2:
            score(score1, score2, turn)
            player += 1
        print(board2)  
    #displays the final score
    thefinal(score1,score2)

main()



