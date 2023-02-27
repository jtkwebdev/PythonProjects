#John Kallis
#jkallis1@umbc.edu
#4/30/2014
#proj2.py
#this program is a bookstore inventory
#lab sec 03, lecture sec 01


#no parameter
#no return
#prints the greeting
def greeting():
	
	print('Welcome to the bookstore program!')

#paraeter:inventory
#no return
#asks for the file inputand makes entries into theInventory
def readdatabase(inventory):
	
	flag = False
	while flag == False:
		file1 = input('enter the name of the file: ')
		flag = filecheck(file1)
	#the 2d list used to make the dictionary
	mylist = create2dlist(file1)

	#seperates the 2d list into the keys and values
	for i in range(len(mylist)):
		if mylist[i][0] not in inventory:
			#adds the author as a key in the inventory
			inventory[mylist[i][0]] = []
			#adds the values to the inventory
			inventory[mylist[i][0]].append(mylist[i][1:])
		else:
			#adds the values to the inventory
			inventory[mylist[i][0]].append(mylist[i][1:])

#parameter: file1
#returns mylist2 (a 2d list)
#brings in the file name and returns a 2D list
#using 3 for loops
def create2dlist(file1):

	mylist = []
	mylist2 = []
	inputfile = open(str(file1), 'r')
	for i in inputfile:
		i = i.title()
		mylist.append(i.strip())
	inputfile.close()
	for j in mylist:
		j = j.title()
		mylist2.append(j.split(','))
	for i in range(len(mylist2)):
		mylist2[i][0] = mylist2[i][0] + ', ' + mylist2[i][1]
		del mylist2[i][1]
	
	return mylist2

#parameter: file1
#returns true or false
#checks the file input. returns bool
def filecheck(file1):

    try:
        inputfile = open(str(file1), 'r')
        return True
    except:
    	print('error reading database')
    	return False

#no parameter
#returns the choice
#prints the menu and gets the choice
def printmenu():

	flag = False
	print()
	print('---------------------')
	print('Enter 1 to display the inventory')
	print('Enter 2 to display to books by one author')
	print('Enter 3 to add a book')
	print('Enter 4 to change the price')
	print('Enter 5 to change the qty on hand')
	print('Enter 6 to view the total number of books in the inventory')
	print('Enter 7 to see the total amount of the entire inventory')
	print('Enter 8 to exit')

	while flag == False:
		choice = input('Enter your choice:')
		flag = choicecheck(choice)
	choice = str(choice)
	return choice

#parameter: choice
#returns true or false
#checks choice input and returns a bool
def choicecheck(choice):

	try:
		choice = int(choice)
		if choice in range(1,9):
			return True
		else:
			return False
	except:
		return False
	

#parameter: inventory
#no return
#display the inventory
#choice 1
def displayinventory(inventory):



	for i in sorted(inventory):
		print('The author is: ', i)
		print()
		for j in sorted(inventory[i]):
			print('	The title is:', j[0])
			print('	The qty is:', j[1])
			print('	The price is:', j[2])
			print()
			print('	---')
			print()

#parameter: inventory
#no return
#displays the inputed authors work
#choice 2
def displayauthorswork(inventory):
	
	flag = False
	name = makethename()
	for i in inventory:
		if i == name:
			flag = True

	if flag == False:
		print('Sorry no books by author ' + name + ' in the inventory')	
	else:
		for j in sorted(inventory[name]):
		
			print('	The title is', j[0])
			print('	The qty is:', j[1])
			print('	The price is:', j[2])
			print()
			print('	---')
			print()

#paramater: inventory
#adds a book to the inventory
#no return
#choice 3
def addbook(inventory):
	
	flag = False
	name = makethename()

	#checks if the author is in the inventory already
	for i in inventory:
		if i == name:
			flag = True

	#gets the input for the title name then changes it to the correct format
	Title = input('Enter the title: ')
	Title = Title.title()

	#for if the author IS NOT in the invenetory
	if flag == False:
		qty = loopqty()
		price = loopprice()
		inventory[name] = [[Title, qty, price,]]

	#for if the author IS in the inventory
	else:
		#checks if the book is in the inventory
		for i in inventory[name]:
			if Title == i[0]:
				print('This book is alreaady in the inventory and cannot be added again')
				flag = False
		#for if the book is not in the inventory
		#we get the rest of the values and add them to the inventory
		if flag == True:
			qty = loopqty()
			price = loopprice()
			print(price)
			
			inventory[name].append([Title, qty, price])

#no parameter
#returns the name formated
#gets the input for the authors first and last name and 
#returns the name in the correct case
def makethename():

	fname = input("Enter the author's first name: " )
	lname = input("Enter the author's last name: ")
	name = lname + ', ' + fname
	name = name.title()

	return name

#no parameter
#loops the qty input and 
#returns a valid qty
def loopqty():

	flag = False
	while flag == False:
		qty = input('Enter the qty: ')
		#checks if the qty is a positive whole number
		try:
			qty = int(qty)
			if qty >= 0:
				flag = True
			else:
				print('Invalid input for the qty')
		except:
			print('Invalid input for the qty')

	return qty
#no parameter
#loops the qty input and 
#returns a valid qty
def loopnewqty():

	flag = False
	while flag == False:
		qty = input('Enter the qty: ')
		#checks if the qty is a positive whole number
		try:
			qty = int(qty)
			if qty >= 0:
				flag = True
			else:
				print('Invalid input for the new qty')
		except:
			print('Invalid input for the new qty')

	return qty

#no parameter
#loops the price input and 
#returns the price
def loopprice():

	flag = False
	while flag == False:
		price = input('enter the price: ')
		cost = price
		check = False
		#checks if the price is a float
		try:
			price = float(price)
			#checks if the price is positive
			if price >= 0:
				check = True
			else:
				print('Invalid input for the price')
			#if the price is positve
			if check == True:
				#checks if the price is exactly 2 digits
				

				if cost[-3] == '.':
					flag = True
				else:
					print('Invalid input for the price')
		except:
			print('Invalid input for the price')
	return cost

#no parameter
#loops the price input and 
#returns the price
def loopnewprice():

	flag = False
	while flag == False:
		price = input('enter the price: ')
		cost = price
		check = False
		#checks if the price is a float
		try:
			price = float(price)
			#checks if the price is positive
			if price >= 0:
				check = True
			else:
				print('Invalid input for the new price')
			#if the price is positve
			if check == True:
				#checks if the price is exactly 2 digits
				

				if cost[-3] == '.':
					flag = True
				else:
					print('Invalid input for the new price')
		except:
			print('Invalid input for the new price')
	return cost


#parameter: inventory
#no return
#changes the price of a book in the inventory
#choice 4
def changeprice(inventory):
	
	flag = False
	flag2 = False
	name = makethename()
	#checks if the author is in the inventory
	for i in inventory:
		if i == name:
			flag = True
	#if the author IS NOT in the inventory
	if flag == False:
		print('No such author in your database. So you cannot change the price')	
	
	#if the author IS in the inventory
	else:
		#get the title name
		Title = input('Enter the title: ')
		Title = Title.title()		
		
		#checks if the title is in the inventory
		for i in inventory[name] :
			#if it is
			if i[0] == Title:
				price = loopnewprice()
				flag2 = True
				print('Price will be updated from ', i[2], 'to', price)
				i[2] = price

		#f the title isnt in the inventory
		if flag2 == False:
			print('No book with the title ' + Title + ' by ' + name + ' in inventory')

#parameter: inventory
#no return
#changes the qty of a book in the inventory
#choice 5
def changeqty(inventory):
	
	flag = False
	name = makethename()
	#checks if the author in the inventory
	for i in inventory:
		if i == name:
			flag = True
	#if the author IS NOT in the inventory
	if flag == False:
		print('Sorry no books by author ' + name + ' in the inventory')	
	#if the author IS in the inventory
	else:

		Title = input('Enter the title: ')
		Title = Title.title()
		#checks if the title IS in the inventory
		for i in inventory[name] :
			#if it IS
			if i[0] == Title:
				qty = loopnewqty()
				flag = False
				print('Qty will be updated from ', i[1], 'to', qty)
				i[1] = qty
		#if its NOT
		if flag == True:
			print('Author has no book titled '+ Title)

#parameter: inventory
#no return
#displays the total quantity of the books in the inventory
#choice 6
def totalqty(inventory):
	
	total = 0
	for i in inventory:
		for j in inventory[i]:
			#adds up all of the qtys of every book in the inventory
			total += int(j[1])
	print('The total number of books is ', total)

#parameter: inventory		
#no return
#dispays the total worth of the inventory
#choice 7
def calculatetotalamount(inventory):
	
	total = 0
	for i in inventory:
		for j in inventory[i]:
			#mulitplies the price and the qty of everybook and
			#adds it to the total worth
			total += float(j[2])*int(j[1])
	print('The total inventory is worth $', '%.2f' % total)

#brings everything together
def main():
	
	#print greeting
	greeting()
	
	#dictionary to hold the inventory
	theInventory = {}

 	#put the data in the file into the dictionary 
	readdatabase(theInventory)

	flag = False

 	#keep looping till flag is set to False 
	while flag == False: 
 
		choice = printmenu()

		if choice=="1": 
 			displayinventory(theInventory) 
		elif choice=="2": 
 			displayauthorswork(theInventory) 
		elif choice=="3": 
 			addbook(theInventory) 
		elif choice=="4": 
 			changeprice(theInventory) 
		elif choice=="5": 
 			changeqty(theInventory) 
		elif choice=="6": 
 			totalqty(theInventory) 
		elif choice=="7": 
 			calculatetotalamount(theInventory) 
		elif choice=="8": 
 			print ("Thank you for using this program") 
 			flag = True
		else: 
 			print ("Invalid choice") 

main()