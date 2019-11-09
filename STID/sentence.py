"""
Author : Paul Mathieu (/paul-mathieu)

In this file, you can find Python programs in one line to play with strings.
All of these programs were done during my first year of learning Python.

"""

#
#==============================================================================
#  Repeat a sentence
#==============================================================================
#


# One Line script

def repeatSentence(sentence, number):
    print(*["\n" + str(sentence) for repeat in range(number)])


# Normal Script

def repeatSentenceEasy(sentence, number):
    for repeat in range(number):
        print("\n" + str(sentence))


# Tests

#repeatSentence("I like to move it, move it !", 3)



#
#==============================================================================
#  
#==============================================================================
#


# One Line script

def sentenceToCamel(phrase):
    return "".join(x + y for x, y in zip(phrase[::2].upper(), phrase[1::2].lower()))


# Normal Script

def sentenceToCamelEasy(phrase):
    
    #initialization of the variable that will be returned
    string = ""
    
    #for each element of the string,
    #if it is even, it will be returned in upper case
    #else it will be returned in lower case
    for k in range(len(phrase)):
        if k%2 == 0:
            string += phrase[k].upper()
        else:
            string += phrase[k].lower()
    
    return string


# Tests

#print(sentenceToCamel('My name is Paul'))










