"""
Author : Paul Mathieu (/paul-mathieu)

In this file, you can find Python programs in one line to play with strings.
All of these programs were done during my first year of learning Python.

"""


def repeatSentence(sentence, number):
    print(*["\n" + str(sentence) for repeat in range(number)])

#repeatSentence("I like to move it, move it !", 3)
    
def repeatSentenceEasy(sentence, number):
    for repeat in range(number):
        print("\n" + str(sentence))
