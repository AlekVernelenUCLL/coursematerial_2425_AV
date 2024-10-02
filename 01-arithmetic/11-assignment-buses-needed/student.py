# write your code here
from math import ceil
def buses_needed(people_count, bus_capacity):
    result = ceil(people_count/bus_capacity)
    return result