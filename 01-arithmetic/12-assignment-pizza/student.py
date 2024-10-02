# write your code here
from math import ceil
def pizza(n_people, slices_per_pizza):
    result = ceil(n_people/slices_per_pizza)
    return result