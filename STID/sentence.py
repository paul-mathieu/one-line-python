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
#  Convert a sentence in Camelcase
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



#
#==============================================================================
#  Palindrome
#==============================================================================
#


# One Line script

def isPalindrome_v1(string):
    return string == string[::-1]

def isPalindrome_v2(string):
    #sum of boolean values : True == 1 and False == 0
    return sum([string[index] != string[len(string) - (index + 1)] for index in range(len(string) - 1)]) == 0

# Normal Script

def isPalindromeEasy(string):
    #for each element of an half string ('semâmes' -> 'sem')
    for index in range(len(string) - 1):
        #if it's the same that the opposit element
        if string[index] != string[len(string) - (index + 1)]:
            return False
    return True

# Tests

#isPalindrome_v2('semâmes')



#
#==============================================================================
#  Number of different letters between two strings
#==============================================================================
#


# One Line script

def marteau(str1, str2):
    return sum(x != y for x, y in zip(str1, str2)) if len(str1) == len(str2) else 'error'


# Normal Script

def marteauEasy(str1, str2):
    
    #if the words aren't the same length
    if len(str1) == len(str2):
        return 'error'
    
    diffLetters = 0
    for index in range(str1):
        if str1[index] != str2[index]:
            diffLetters += 1
    
    return diffLetters
    

# Tests

#marteau('semâmes', 'semions')






