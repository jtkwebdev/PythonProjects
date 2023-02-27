import random

# returned
#DESCRIPTION: checks if the value is prime
def rabinMiller(p):
    
    p=int(p)
    s=p-1
    t=0
    
    if p<2:
        return True#not prime
    elif p==2:
        return False#prime
    elif((p%2)==0):
        return True#not prime
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
def main():
    print(rabinMiller(5714040173))
    print(rabinMiller(243713032363))

main()
