def combine(d1, d2):
    result = dict()
    for en, nl in d1.items():
        if nl in d2:
            result[en] = d2[nl]
    return result

# d1 = {
#     'cat': 'kat',
#     'dog': 'hond',
#     'elephant': 'olifant'
# }
# d2 = {
#     'kat': 'chat',
#     'hond': 'chien',
#     'zeehond': 'phoque'
# }

# print(combine(d1, d2))