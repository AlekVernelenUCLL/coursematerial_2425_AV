def heatwave(temperatures):
    count25 = 0
    count30 = 0
    for temp in temperatures:
        if 25 >= temp < 30:
            count25 += 1
        elif temp > 30:
            count30 += 1
        else:
            count25 = 0
            count30 = 0