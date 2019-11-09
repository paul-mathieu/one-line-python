def genAcidesV1():
    return list(filter((lambda x : x != "UAA" and x != "UAG" and x != "UGA"), list(str(a + b + c) for a in ["A", "C", "G", "U"] for b in ["A", "C", "G", "U"] for c in ["A", "C", "G", "U"])))

def genAcidesV2():
    return [a + b + c for a in ["A", "C", "G", "U"] for b in ["A", "C", "G", "U"] for c in ["A", "C", "G", "U"] if a + b + c not in ["UAA", "UAG", "UGA"]]

