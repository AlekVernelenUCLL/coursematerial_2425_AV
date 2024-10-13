def total_cost(amount):
    if amount < 100:
        amount += 10
    elif amount >= 200:
        amount *= 0.95
    return amount