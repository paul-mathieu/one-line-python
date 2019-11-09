from functools import reduce
def convertToSec(temps):
    return str(reduce(lambda a, b: a * 60 + b, map(int, temps.split(':')), 0)) + " secondes"
