# write your code here
def drop_last_digit(n):
    a = str(n)
    n_digits = len(a)
    index = n_digits-1
    removed_last_digit = a.replace(a[index],'')
    return int(removed_last_digit)

print(drop_last_digit())