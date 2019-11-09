from functools import reduce

#Exercice 1
from random import randint
def hasard():
    k, al = 0, randint(1,10)
    while int(input("Entrez un nombre entre 1 et 10 :\n")) != int(al): k += 1
    print("C'était bin le nombre " + str(al) + " qu'il fallait deviner !\nTu l'a trouvé en " + str(k) + " essais.")
    
#Exercice 2
def factorielle(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

#def listesPuissances(n):
#    return [list(map(lambda x: x(r), [lambda x: x**2, lambda x: x**3]))) for r in range(n)]

def listesPuissances2(n):
    return [[x**p for p in [1,2]] for x in range(10)]

#Exercice 3
def palindrome(s):
    return s == s[::-1]


#Exercice 4
def isInside(c, s):
    print(c in s)


#Exercice 5
def marteau(str1, str2):
    return sum(x != y for x, y in zip(str1, str2)) if len(str1) == len(str2) else 'error'


#Exercice 6
def isEven(x): print(x % 2 == 0)

def isEvenAll(x): return all(map(lambda x: x % 2 == 0, list(int(k) for k in x.split(","))))


#Exercice 7
setMots = {"oiseau","kayak","fromage", "xenon", "armoire","gag", "rotor", "sandwich"}

def triMots(mots): return sorted(mots)

def triMotsByTaille(mots): return sorted(list(mots), key=len)


def triMotsByTailleEtPalin(mots): return list(filter(lambda x: x == x[::-1],list(mots))) + list(filter(lambda x: x != x[::-1],list(mots)))

def triMotsByTailleEtPalin2(mots): return list(filter(lambda x: x == x[::-1], sorted(list(mots)))) + list(filter(lambda x: x != x[::-1],sorted(list(mots))))








def factorielle2(n):
    print(all(map(lambda x: x%2==0, range(n))))

def listesPuissances(n):
    for r in range(n):print(list(map(lambda x: x(r), [lambda x: x**2, lambda x: x**3])))

m = [1,2,3]
n = [1,4,9]

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(x for x in a if x in b))

def fact(n):
    return reduce(lambda x,y: x*y, range(2, n + 1), 1)



a = "1,2,3,5,7,9"

print(list(int(k) for k in a.split(",")))




print(reduce(lambda a, b: a * 60 + b, map(int, input().split(':')), 0) , "secondes")
from datetime import datetime
datetime.now()

