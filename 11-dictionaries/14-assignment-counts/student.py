def counts(xs):
    result = dict()
    for char in xs:
        if result.setdefault(char, 0) > -9:
            result[char] += 1
    return result


