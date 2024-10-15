def is_capitalized(string):
    if bool(string):
        con1 = string[0] == string[0].upper()
        con2 = string[1:] == string[1:].lower()
        return con1 and con2
    return False