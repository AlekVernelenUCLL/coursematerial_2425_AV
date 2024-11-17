def remove_duplicates(xs):
    lst = []
    for num in xs:
        if num not in lst:
            lst.append(num)
    return lst

# setxs = set([1, 1])
# print(setxs)
# lst = list(setxs)
# print(lst)

# a = remove_duplicates([1, 3, 2, 2, 4, 1])
# print(a)