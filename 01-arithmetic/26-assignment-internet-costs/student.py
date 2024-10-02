# write your code here
from math import floor
def internet_costs(duration_in_seconds, cost_per_block):
    x = duration_in_seconds//360
    rest = duration_in_seconds%360
    if rest > 0:
        x += 1
    total_cost = x*cost_per_block
    return total_cost