def heatwave(temperatures):
    count25 = 0
    count30 = 0
    for temp in temperatures:
        if count25 >= 5 and count30 >=3:
            return True
        else:
            if 25 <= temp < 30:
                count25 += 1
            elif temp >= 30:
                count25 += 1
                count30 += 1
            else:
                count25 = 0
                count30 = 0
    if count25 >= 5 and count30 >=3:
        return True
    return False