from math import floor
def thanos(queue_size, target_size):
    count = 0
    while queue_size > target_size:
        queue_size = floor(queue_size/2)
        count += 1
    return count

# a = thanos(100,10)
# print(a)