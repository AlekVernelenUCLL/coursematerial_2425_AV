def gcd(x, y):
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    high = max(x,y)
    low = min(x,y)
    for i in range(1,high+1):
        if high%i==0 and low%i==0:
            den = i
    return den