def is_valid_month(month):
    return 1<=month<=12

def is_leap_year(year):
    yes = year%4==0 or (year%100==0 and year//400==0)
    nott = year%100==0 and year%400!=0
    return yes or nott

def has_30_days(month):