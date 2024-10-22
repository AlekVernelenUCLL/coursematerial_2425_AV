def is_prime(n):
    count = 0
    for i in range(2,n+1):
        if n % i == 0:
            count += 1
    return count == 1