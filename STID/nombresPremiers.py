

def affNbsPremiers(n):
    for a in range(2,n+1):
        #vb = True
        #for b in range(2,math.sqrt(n)+1):
        for b in range(2,int(float(n)**(1/2) + 1.0)):
            if a % b == 0:
                print(str(a+1), end = "\t")
                
                

def affNbsPremiersOL(n):
    print([x for x in range(2, n) if not 0 in map(lambda y : x % y, range(2, int(x**0.5 + 1)))])


