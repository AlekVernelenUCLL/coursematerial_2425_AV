def contains_duplicates(xs):
    if not xs:
        return False
    setxs = set(xs)
    lst = list(setxs)
    return not(lst == xs)



# a = {1,2,3} == {3,2,1}
# print(a)