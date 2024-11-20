def group_by_first_letter(strings):
    result = dict()
    for name in strings:
        first_letter = name[0].upper()
        result.setdefault(first_letter,[]).append(name)
    return result