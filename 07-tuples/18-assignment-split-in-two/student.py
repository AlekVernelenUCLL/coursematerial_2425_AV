def split_in_two(xs):
    half = len(xs) // 2
    if len(xs) % 2 == 0:
        left = xs[:half]
        right = xs[half:]
    else:
        left = xs[:half+1]
        right = xs[half+1:]
    return (left,right)