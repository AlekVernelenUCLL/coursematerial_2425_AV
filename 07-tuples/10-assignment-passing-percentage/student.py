def passing_percentage(grades):
    count = 0
    for grade in grades:
        if grade >= 10:
            count += 1
    return count/len(grades)*100