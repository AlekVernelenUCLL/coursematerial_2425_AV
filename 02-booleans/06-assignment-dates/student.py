def is_valid_month(month):
    return 1<=month<=12

def is_leap_year(year):
    # leap = year%4==0 or (year%100==0 and year%400==0)

    leapyes = (year%4==0 and year%100!=0) or (year%4==0 and year%100==0 and year%400==0)
    return leapyes

def has_30_days(month):
    return is_valid_month(month) and month in (4,6,9,11)

def has_31_days(month):
    return is_valid_month(month) and month in (1,3,5,7,8,10,12)

def has_28_days(month,year):
    return not is_leap_year(year) and month==2

def has_29_days(month,year):
    return is_leap_year(year) and month==2

def is_valid_date(day,month,year):
    validm = is_valid_month(month)
    validd31 = has_31_days(month) and 1<=day<=31
    validd30 = has_30_days(month) and 1<=day<=30
    validd29 = has_29_days(month,year) and 1<=day<=29
    validd28 = has_28_days(month,year) and 1<=day<=28
    validd = validd31 or validd30 or validd29 or validd28
    return validm and validd