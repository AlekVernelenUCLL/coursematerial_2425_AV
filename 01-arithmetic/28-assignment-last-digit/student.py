# write your code here
def last_digit(n):
    a = str(n)
    n_digits = len(a)
    index = n_digits-1
    return int(a[index])