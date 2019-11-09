def dictLettersNumbers(phrase):
    return {"numbers" : reduce(lambda x, y : x + y, list(map(lambda x: x.isdigit(),list(phrase)))), "letters" : reduce(lambda x, y : x + y, list(map(lambda x: x.isalpha(),list(phrase))))}
