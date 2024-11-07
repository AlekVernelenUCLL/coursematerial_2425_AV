def all_equal(xs):
    i = 0
    while i < len(xs) - 1:
        if xs[i] != xs[i + 1]:
            return False
        i += 1
    return True