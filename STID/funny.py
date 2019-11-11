"""
Author : Paul Mathieu (/paul-mathieu)

In this file, you can find Python random programs in one line.
All of these programs were done during my first year of learning Python.

"""



#
#==============================================================================
#  
#==============================================================================
#


# One Line script

#we print a string for each level (thanks to the generator) separated by a \n
def doATree(size):
    print('\n'.join([str((etoile*2+1)*"*").center(size*2-1, " ") for etoile in range(size)]))


# Normal Script

#a function to do the same that : [signe]*n
def repSigne(n, signe):
    bout = ""
    for k in range(n):
        bout = bout + signe
    return bout

#proc to do a tree
def doATreeEasy(size):
    
    #for the first level
    star = 1
    
    #for each level
    #at each level, the number of blanks on each side of the star reduced by one
    for k in range(size):
        size = size - 1
        print(repSigne(size," ") + repSigne(star,"*") + repSigne(size," "))
        star = star + 2


#or an other script

def doATreeEasy2(size):
    etoile = 1
    for k in range(size):
        print(str(etoile*"*").center(size*2-1, " ") )
        etoile = etoile + 2


# Tests

#doATree(10)



#
#==============================================================================
#  
#==============================================================================
#


# One Line script

def genAcides_V1():
    return list(filter((lambda x : x != "UAA" and x != "UAG" and x != "UGA"), list(str(a + b + c) for a in ["A", "C", "G", "U"] for b in ["A", "C", "G", "U"] for c in ["A", "C", "G", "U"])))

def genAcides_V2():
    return [a + b + c for a in ["A", "C", "G", "U"] for b in ["A", "C", "G", "U"] for c in ["A", "C", "G", "U"] if a + b + c not in ["UAA", "UAG", "UGA"]]


# Normal Script

def genAcidesEasy():
    acidsList = []
    letters = ["A", "C", "G", "U"]
    
    for a in letters:
        for b in letters:
            for c in letters:
                if a + b + c not in ["UAA", "UAG", "UGA"]:
                    acidsList.append(a + b + c)
                    
    return acidsList

# Tests

#genAcides_V2()



#
#==============================================================================
#  Playing Poker !
#==============================================================================
#


# One Line script

from random import randint

def listeCartes():
    return [str(a) + " de " + str(b) for b in ["Coeur", "Carreau", "Trefle", "Pique"] for a in list(range(2,11)) + ["Valet", "Dame", "Roi", "As"] ]


# Normal Script



# Tests












