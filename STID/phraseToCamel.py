
def phraseToCamel(phrase):
    for k in range(len(phrase)):
        if k%2 == 0:
            print(phrase[k].upper(), end = "")
        else:
            print(phrase[k].lower(), end = "")


def phraseToCameOL(phrase):
    "".join(x + y for x, y in zip(phrase[::2].upper(), phrase[1::2].lower()))
