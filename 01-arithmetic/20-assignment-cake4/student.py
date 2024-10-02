# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    cake_eggs = eggs//eggs_per_cake
    cake_flour = flour//flour_per_cake
    cake_butter = butter//butter_per_cake
    cake_sugar = sugar//sugar_per_cake
    return min(cake_eggs,cake_flour,cake_butter,cake_sugar)