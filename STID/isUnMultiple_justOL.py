def isUnMultiple(x, y):
    return str(x) + " est un multiple de " + str(y) if x in list(range(500))[::y] else str(x) + " n'est pas un multiple de " + str(y)
