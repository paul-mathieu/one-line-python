def isEvenAll(x):
    return all(map(lambda x: x % 2 == 0, list(int(k) for k in x.split(","))))

