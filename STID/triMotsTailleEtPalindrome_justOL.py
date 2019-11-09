def triMotsByTailleEtPalin(mots):
    return list(filter(lambda x: x == x[::-1],list(mots))) + list(filter(lambda x: x != x[::-1],list(mots)))

def triMotsByTailleEtPalin2(mots):
    return list(filter(lambda x: x == x[::-1], sorted(list(mots)))) + list(filter(lambda x: x != x[::-1],sorted(list(mots))))
