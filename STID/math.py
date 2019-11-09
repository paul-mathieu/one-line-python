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



#
#==============================================================================
#  Give all prime numbers up to a fixed value
#==============================================================================
#


# One Line script

def nPrimeNumbers(n):
    return [x for x in range(2, n) if not 0 in map(lambda y : x % y, range(2, int(x**0.5 + 1)))]


# Normal Script

def nPrimeNumbersEasy(n):
    
    liste = []
    
    for number in range(n + 1): 
          
       #if num is divisible by any number between 2 and number, it's not a prime  
       if number > 1: 
           for n in range(2, number): 
               if (number % n) == 0: 
                   break
           else: 
               liste.append(number)
    
    return liste


# Tests

#nPrimeNumbers(100)













