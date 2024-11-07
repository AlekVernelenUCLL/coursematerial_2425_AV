def split_name(full_name):
    i = 0
    for char in full_name:
        i += 1
        if char == " ":
            first = full_name[:i-1]
            last = full_name[i:len(full_name)]
    result = (first,last)
    return result

print(split_name("Walter White"))