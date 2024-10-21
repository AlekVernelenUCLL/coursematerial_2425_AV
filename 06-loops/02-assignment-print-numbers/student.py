def print_numbers(start, stop, step):
    result = start
    i = 0
    while result < stop:
        result = start+i*step
        if result < stop:
            print(result)
            i += 1

# print_numbers(1,5,1)