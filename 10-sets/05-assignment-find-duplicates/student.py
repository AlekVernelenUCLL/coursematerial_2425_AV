def find_duplicates(xs):
    set_xs = set(xs)
    duplicates = []
    for num in xs:
        if num in set_xs:
            set_xs.remove(num)
        else:
            duplicates.append(num)
    set_dup = set(duplicates)
    lst_dup = list(set_dup)
    return lst_dup

# a = find_duplicates([1, 2, 1, 3, 2, 1, 1])
# [1, 2]

# print(a)