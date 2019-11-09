#Exercice 1
def prgmNom():
    #print("\nBienvenue à toi, " + input("Comment t'appelles-tu ? \n"))
    print("\nBienvenue à toi, %s" % input("Comment t'appelles-tu ? \n"))
    #print("Bonjour, %s " % input("Comment t'appelles-tu ? \n"))

#Exercice 2
def prgmMoveItWhile():
    k = 0
    nombre = int(input("Nombre ?\n"))
    while k != nombre:
        print("I like to move it, move it")
        k = k + 1

def prgmMoveItFor(n):
    for k in range(int(n)):
        print("I like to move it, move it", end=". ")
#prgmMoveItFor(input("Nombre ?\n"))

#oneLiner
#print(*["\nI like to move it, move it" for x in range(int(input("Nombre ?\n")))])

#Execice 3
def isPair(n):
    print(str(int(n)) + " est un nombre", end = " ")
    if int(n) % 2 == 0:
        print("pair.")
    else:
        print("impair.")

def isPairOL(n):
    print(str(int(n)) + " est un nombre " + ["pair" if int(n) % 2 == 0 else "impair"][0] + ".")
    #print("pair") if int(n) % 2 == 0 else print("impair")
    
#Exercice 4
def chaineDeuxNombres():
    a, b = input("Entrez deux nombres, séparés par une vigule :\n").split(",")
    print(a)
    print(b)

def chaineNombresOL(a):
    print("".join(x + y for x, y in zip(a.split(','),'\n'*len(a))))

#chaineNombresOL('1,2,3')


#Exercice 5
def repSigne(n, signe):
    bout = ""
    for k in range(n):
        bout = bout + signe
    return bout

def sapin(taille):
    etoile = 1
    for k in range(taille):
        taille = taille - 1
        print(repSigne(taille," ") + repSigne(etoile,"*") + repSigne(taille," "))
        etoile = etoile + 2

def sapin2(taille):
    etoile = 1
    for k in range(taille):
        print(str(etoile*"*").center(taille*2-1, " ") )
        etoile = etoile + 2

#on print le string des étages (générés avec le générateur) séparé par un \n
def sapin2OL(taille):
    print('\n'.join([str((etoile*2+1)*"*").center(taille*2-1, " ") for etoile in range(taille)]))


def sapin2OLx(taille):
    for etoile in range(taille):
        print(str((etoile*2+1)*"*").center(taille*2-1, " "))

#print('\n'.join((['0','1','2','3','4'][a] for a in range(5))))


#Exercice 6
phrase = "Mon nom est Paul"
#[i for i in phrase]

def phraseToCamel(phrase):
    for k in range(len(phrase)):
        if k%2 == 0:
            print(phrase[k].upper(), end = "")
        else:
            print(phrase[k].lower(), end = "")

#probleme
def phraseToCame2(phrase):
    print("".join(x + y for x, y in zip(phrase[::2].upper(), phrase[1::2].lower())))


#Exercice 7

def affNbsPremiers1(n):
    for a in range(2,n+1):
        #vb = True
        #for b in range(2,math.sqrt(n)+1):
        for b in range(2,int(float(n)**(1/2) + 1.0)):
            if a % b == 0:
                print(str(a+1), end = "\t")
                
                

def affNbsPremiers2(n):
    print([x for x in range(2, n) if not 0 in map(lambda y : x % y, range(2, int(x**0.5 + 1)))])


def affNbsPremiers3(n):
    n = 0
    listP = []
    for k in range(2,int(n)):
        for l in range(l+1,int(n)+1):
            a
        



##var k, l, n = 0,no , t = [], t2 = [], l, h;
##no = proglab.inputNumber("n ?");
##for (k = 2; k <= no-1; k++) {t[k] = k + 1} //valeurs affectées au tableau t[]
##for (k = 2; k <= no-1; k++) {             //tous les pas premiers remplacés par 0
##  for (l = k + 1; l <= no-1; l++) {
##      if (t[l] % k == 0) {t[l] = 0}}}
##for (k = 2; k <= no-1; k++) {             //tous les non 0 dans le tableau t2[]
##  if (t[k] != 0) {t2[n] = t[k];n=n+1}}
##for (k=n;k<=n+(10-(n%10));k++) {t2[k]=0}  //nb valeurs ds t2[] est un multiple de 10
##l=n
##for (k=0;k<=n;k=k+10) {                   //affichage t2[] avec lignes de 10 valeurs
##  for (h=k;h<=k+10;h++) {
##      if (t2[h]!=0) {proglab.print(t2[h]+", ")}}
##  proglab.print("\n")}


















