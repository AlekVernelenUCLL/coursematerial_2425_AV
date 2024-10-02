# write your code here
def cake3(eggs, flour, butter, sugar):
    cake_eggs = eggs//5
    cake_flour = flour//250
    cake_butter = butter//200
    cake_sugar = sugar//250
    return min(cake_eggs,cake_flour,cake_butter,cake_sugar)