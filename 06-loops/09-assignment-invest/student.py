def invest(amount, rate, goal):
    count = 0
    while amount < goal:
        amount *= 1+rate/100
        count += 1
    return count