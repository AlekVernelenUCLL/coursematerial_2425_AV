def years_to_target(amount,interest,target):
    years = 0
    while amount < target:
        amount *= 1+(interest/100)
        years += 1
    return years

# print(years_to_target(500,5,1000))