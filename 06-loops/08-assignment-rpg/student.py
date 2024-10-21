def rpg2(n_sides,goal):
    for i in range(1,n_sides+1):
        for j in range(1,n_sides+1):
            sum = i+j
            if sum >= goal:
                count += 1


# def rpg3(n_sides,goal):
#     for i in range(1,n_sides+1):
#         rpg2(n_sides,goal)


