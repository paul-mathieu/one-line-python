#Exercice 1

def rep1(val):
    return [val] * 30


#Exercice 2

def genAlea():
    print({a for a in range(1000) if a%7 == 0 and a%5 == 0})


#Exercice 3

people = [("Marc", "Jacob", 1958) , ("Jean", "Bonneau", 1963), ("Elisabeth", "London", 1981), ("Didier","Deschamps", 1998)]

def pna(liste):
    print([(p[0][0]+p[1][0], 2018 - p[2]) for p in liste])


#Exercice 4

def compterLettres(phrase):
    print(dict([(x, phrase.count(x)) for x in phrase]))


#Exercice 5

acides = [ "A", "C", "G", "U"]

def genAcides(liste):
    return list(filter((lambda x : x != "UAA" and x != "UAG" and x != "UGA"), list(str(a + b + c) for a in liste for b in liste for c in liste)))


#Exercice 6

from random import randint

def listeCartes():
    return [str(a) + " de " + str(b) for b in ["Coeur", "Carreau", "Trefle", "Pique"] for a in list(range(2,11)) + ["Valet", "Dame", "Roi", "As"] ]

liste = listeCartes()
def genAlea(liste):
    from random import randint
    a = randint(0,len(liste))
    carte = liste[a]
    liste.remove(carte)
    return carte, list

def genAlea1(nb, liste):
    return list(map(lambda x: x(nb), [lambda y: liste[y], lambda y: list(filter(lambda z : z != liste[y], liste))]))

lambda nb, liste : list(map(lambda x: x(nb), [lambda y: liste[y], lambda y: list(filter(lambda z : z != liste[y], liste))]))

#def nCartesAlea(nb):
#    return dict(zip(["Joueur 1 : ", "Joueur 2 : ", "Joueur 3 : ", "flop : ", "turn : ", "river : "], ))


#print([list(range(a)) for a in [3] * nbJoueurs + [3,1,1]])    >>>   [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0], [0]]

#list(map(len,[list(range(a)) for a in [3] * nbJoueurs + [3,1,1]]))    >>>   [3, 3, 3, 1, 1]

nbJoueurs = 2


def listeCartesTest(liste, nbJoueurs):
    nbCartesTirees = [3] * nbJoueurs + [3,1,1]
    listeCarteT = []
    for a in range(nbCartesTirees):
        listeCarteJ = []
        for b in range(nbCartesTirees[a]):
            x, liste = genAlea(liste)
            listeCarteJ = listeCarteJ + [x]
        listeCarteT = listeCarteT + [listeCarteJ]
    dict(zip(["Joueur 1 : ", "Joueur 2 : ", "Joueur 3 : ", "flop : ", "turn : ", "river : "], listeCarteT))    


def listeCartesTest2(n):
    return [a for a in 1]


a, b = liste[randint(0,len(liste))], liste.remove(liste[randint(0,len(liste))])


from random import randint


list(map(lambda x: x(randint(0,len(liste))), [lambda y: liste[y], lambda y: list(filter(lambda z : z != liste[y], liste))]))

