"""
Author : Paul Mathieu (/paul-mathieu)

In this file, you can find Python programs in one line to play with strings.
All of these programs were done during my first year of learning Python.

"""


#
#==============================================================================
#  Type of a Number
#==============================================================================
#


# One Line script

def evenOrOdd(n):
    print(str(int(n)) + " est un nombre " + ["pair" if int(n) % 2 == 0 else "impair"][0] + ".")


# Normal Script

def evenOrOddEasy(n):
    print(str(int(n)) + " est un nombre", end = " ")
    if int(n) % 2 == 0:
        print("pair.")
    else:
        print("impair.")


# Tests

#evenOrOdd(10)



#
#==============================================================================
#  Print Elements of a String
#==============================================================================
#


# One Line script

def elementsOfString(a):
    print("".join(x + y for x, y in zip(a.split(','),'\n'*len(a))))


# Normal Script

def elementsOfStringEasy():
    liste = input("Entrez deux nombres, séparés par une vigule :\n").split(",")
    for element in liste:
        print(element)


# Tests

#chaineNombresOL('1,2,3')











