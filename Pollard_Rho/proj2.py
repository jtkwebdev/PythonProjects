#John Kallis
#11/25/2015
#CMSC  441 Marron
#jkallis1@umbc.edu
#project 2 part 1a
#generating public and private RSA keys from input
#and signing message with these generated keys
#descriptions of algorithms will print to screen

import sys
import random

#DESCRIPTION: prints the greeting
def greeting():
	print()
	print("This program generates RSA keys public and private.")
	print("CMSC 441 project 2 part 1a by John Kallis")
	print()

#IN: the  value p is passed into the funcion
#OUT: a boolean is returned
#DESCRIPTION: checks if the value is prime
def rabinMiller(p):
	
	p=int(p)
	s=p-1
	t=0
	
	if p<2:
		return True		#not prime
	elif p==2:
		return False	#prime
	elif((p%2)==0):
		return True		#not prime
	while (s%2)==0:
		s=s//2
		t+=1

	for j in range(1,s):
		a=random.randrange(1,s)
		r=pow(a,s,p)
		if r!=1:
			i=0
			while (r!=(p-1)):
				if (i==(t-1)):
					return True
				else:
					i+=1
					r=pow(r,2,p)
	return False

#IN:max value for range of prime from commandline
#OUT:returns the prime 
#DESCRIPTION:generates a random number then calls isprime(p)
############ to check and returns the prime when it is found
def randomPrimeGenerator(maxValue):
	low = (2**(maxValue-1))
	high = (2**(maxValue))
	prime=random.randrange(low,high)
	while (rabinMiller(prime)):
		prime=random.randrange(low,high)
	return prime
	
#IN: 2 integer values to find gcd, x and y
##### that satify the equation gcd(a,b)=ax+by
#OUT: returns the values for x,y and the gcd
#DESCRIPTION: finds the greatest common divisor 
def extendedEuclid(a,b):
	if b==0:
		return (a,1,0)
	else:
		(d1,x1,y1)=extendedEuclid(b,(a%b))
		(d,x,y)=(d1,y1,(x1-(a//b)*y1))
		return (d,x,y)

#IN: the values for e and t
#OUT: the value for d (the private key)
#DESCRIPTION: returns the modular multipicative inverse
#############of the input (e and t)
def modMultInv(e,f):
	(d,x,y) = extendedEuclid(e,f)
	if (d!=1):
		print("inverse doesn't exist")
		exit()
	else:
		return (x%f)

#IN: a message is passed in
#OUT: the encoded message is returned
#DESCRIPTION: endcodes a message for signiture
def encodeToInt(M):
	x = 0
	for c in M:
		x = x<<8
		x=x^ord(c)	
	return x

def main():	

	greeting()
	maxValue = sys.argv[1]
	maxValue=int(maxValue)

	print()
	#first prime 'p'
	p=randomPrimeGenerator(maxValue)
	#second prime 'q'
	q=randomPrimeGenerator(maxValue)
	#if p=q there is an error
	#most likely the input was to small
	if (p==q):
		print("error p=q")
		exit()

	n=p*q #n=pq used for public key
	t=((p-1)*(q-1)) #phi(n)=(p-1)(q-1)
	e=randomPrimeGenerator(t) #public key
	d=modMultInv(e,t)	#private key
	print("first random prime-p: ",p)
	print()
	print("second random prime-q: ",q)
	print()
	print("n=pq: ",n)
	print()
	print("public key    e: ",e)
	print()
	print("phi(%d): %d"%(n,t))
	print()
	print("private key   d: ",d)
	print()
	print()
	M="I deserve an A"
	print(M)
	g=encodeToInt(M)
	print("message as int: ",g)
	h=pow(g,d,n)
	print("encrypted value with private key d=%d: %d" % (d,h))

#https://www.python.org/download/releases/2.3.5/notes/

#https://en.wikipedia.org/wiki/Karatsuba_algorithm
	print()
	print()
	print("**********MULITPCATION IN PYTHON*********")
	print("python uses the Karatsuba algorithm for multiplying very long ints")
	print("Karatsuba algorithm has a time complexity of O(n**(ln(3))) as opposed")
	print("to the classical algorthim which is O(n^2).")
	print()
	print("**************MODULAR REDUCTION IN PYTHON***************")
	print("python uses the % operator for modular reduction. This method points")
	print("to underlying C libraries")
	print()
	#http://aditya.vaidya.info/blog/2014/06/27/modular-exponentiation-python/
	print("**************MODULAR EXPONENTATION IN PYTHON***************")
	print("The built in method of pythons modular exponentation is pow(x,y,[z])")
	print("where the solution to ((x**y) mod z) is returned. This method points also to")
	print("underlying C libraries which implemnt iterative binary exponentation")
	print()
main()
