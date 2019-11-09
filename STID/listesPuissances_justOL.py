
def listesPuissances2et3(n):
    return [list(map(lambda x: x(r), [lambda x: x**2, lambda x: x**3])) for r in range(n)]

