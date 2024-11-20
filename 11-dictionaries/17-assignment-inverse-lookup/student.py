def inverse_lookup(dictionary, value):
    result = set()
    for key, d_value in dictionary.items():
        if d_value == value and d_value not in result:
            result.add(key)
    return list(result)

a = inverse_lookup({'a': 1, 'b': 1, 'c': 2}, 2)
print(a)