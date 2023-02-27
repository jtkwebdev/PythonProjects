###############################3
#John Kallis
#CMSC 441
#Project 2
#jkallis1@umbc.edu 
#Pollard Rho algorithm
#################
#before build on gl first enable python3 with:
#    scl enable python33 bash
#then build with: 
#		python pollard_rho.py <coprime>
#where it says coprime enter a value only
########(no barckets)
##################################
##################################
########PRIME FACTORS#############
##################################
#test80:
######  1392586057605831118799 = 
############  ((5714040173)*(243713032363))
######################################
#test100:
######  197854876186300186584002542069 = 
##########  ((773097787940011)*(255924773389279))
################################################
#test140:
######  12501831755593877685146576909227993 =
#############
#############################################
#test160:
#######  612354682925704350111656178364155557488904147473 =
###########
##########################################3
#test180:
#######  20964710622122491833169927781113614069887601934227343 =
###############
#######################################
#test200:
#######  415059652915068276200909545813592129413531010425612143823439 =
#############
#loganberry:
######  1082320955021720198454660061583 =
##########
#########################################
#########################################
#########################################
import random
import fractions
import sys
#############################################
#IN: that value n is passed in as a parameter
###### n is a coprime to be factored
#OUT: myList is returned
###	myList contains every value d that was printed
#### d contains possible prime factors of n
#DESCRIPTION: pollard_rho(n) is an algorithms designed
#### by pollard to find the prime factors of a coprime, n,
##### in this case n is very large
### This algorithm is modified from the one provided
#### in our textbook
##########################################
def pollard_rho(n):
	i=1
	x=list()
	y=list()
	x.append(0)
	x.append(random.randrange(0,(n-1)))
	y.append(x[i])
	myList=list()
	j=0
	k=2
	m=n**0.5
	while(i<m):
		i+=1
		x.append(((x[i-1]**2)-1)%n)
		d=fractions.gcd(abs(y[j]-x[i]),n)
		if((d!=1)and(d!=n)):
			print("d: %d"%d) #prints the possible solution to the screen
			count=0 #counter to make sure d is only saved once
			print(i)
			for z in myList: 
				if(d==z):
					count+=1 #adds 1 if d is in the list already
			#d isn't in the list so add it
			if(count==0):	
				myList.append(d)

		if(i==k):
			y.append(x[i])
			j+=1
			k*=2
	#returns the list of factors
	return myList

#################################
####MAIN FUNCTION################
#IN: a value must be passed in
###### on the command line
#################################
def main():
	n=sys.argv[1]  #initializes the commandline argument
	n=int(n) 		#sets the string to an int
	primes=pollard_rho(n) #calls the pollard_rho function which returns a list
	print("factors are:")
	for i in primes:
		print(i)
	#multiplies all of the values against each other to check answer
	for j in range(len(primes)):
		for k in range(len(primes)):
			if(j==k):
				pass
			elif((primes[j]*primes[k])==n):
				print("the 2 primes are ",primes[j]," and ",primes[k])

main()
