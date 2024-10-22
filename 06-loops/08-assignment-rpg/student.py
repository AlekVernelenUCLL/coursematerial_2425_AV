def rpg2(n_sides,goal):
    numb = 0
    count = 0
    for i in range(1,n_sides+1):
        for j in range(1,n_sides+1):
            sum = i+j
            numb += 1
            if sum >= goal:
                count += 1
    return count/numb*100

def rpg3(n_sides,goal):
    numb = 0
    count = 0
    for i in range(1,n_sides+1):
        for j in range(1,n_sides+1):
            for k in range(1,n_sides+1):
                sum = i+j+k
                numb += 1
                if sum >= goal:
                    count += 1
    return count/numb*100