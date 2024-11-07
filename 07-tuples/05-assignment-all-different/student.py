def all_different(xs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j and xs[i] == xs[j]:
                return False
    return True


# xs = (2,4,1,3)
# print(all_different(xs))