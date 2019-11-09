#Exercice 1

rib = '15038012091341531802524'

def isRibValid(rib):
     return len(str(rib)) == 23 and int(rib[len(rib)-2:]) == 97 - (89 * int(rib[:5]) - 15 * int(rib[5:10]) - 3 * int(rib[10:21])) % 97


#Exercice 2

team = ("Lloris", "Pavard", "Matuidi", "Pogba", "Kanté", "Dembélé", "Thauvin", "Griezmann", "Payet", "Giroud", "Mbappé")

def affJoueur(liste):
    print(">".join(team[:-5:-1]))

def ajouter(liste, nom):
    return tuple(list(liste) + [nom])
    
def supprimer(liste, nom):
    return tuple(filter(lambda nom: nom != nom, team))


#Exercice 3

phrase = 'Je suis 007'

from functools import reduce

#reduce(lambda x, y : x + y, list(map(lambda x: x.isdigit(),list(phrase))))
#print(reduce(lambda x, y : x + y, list(map(lambda x: x.a(),list(phrase)))) for a in range(('isdigit', 'isalpha')))
#reduce(lambda x, y : x + y, list(map(lambda x: x.isdigit(),list(phrase))))

def compterLettreChiffres(phrase):
    print("nombres : " +
          str(reduce(lambda x, y : x + y, list(map(lambda x: x.isdigit(),list(phrase))))) +
          " et lettres : " +
          str(reduce(lambda x, y : x + y, list(map(lambda x: x.isalpha(),list(phrase)))))
          )

def compterLettreChiffres2(phrase):
    print("nombres : " +
          str(sum(list(map(lambda x: x.isdigit(),list(phrase))))) +
          " et lettres : " +
          str(sum(list(map(lambda x: x.isalpha(),list(phrase)))))
          )








