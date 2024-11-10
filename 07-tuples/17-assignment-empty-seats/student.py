def empty_seats(used_seats):
    result = 0
    for i in range(len(used_seats)-1):
        unused = used_seats[i+1]-used_seats[i]-1
        result += unused
    return result