def subtuple(xs, ys):
    count = 0
    i = 0
    j = 0
    if ys == ():
        return True
    while i < len(xs):
        if xs[i] == ys[j]:
            count += 1
            if j == len(ys)-1:
                break
            else:
                j += 1
        else:
            count = 0
        i += 1

    return count == len(ys)

# print(subtuple((1, 2, 3, 4, 5), (2, 3, 4)))