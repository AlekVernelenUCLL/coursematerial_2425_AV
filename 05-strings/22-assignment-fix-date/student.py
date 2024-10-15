def fix_date(date):
    mm = date[:2]
    dd = date[3:5]
    yyyy = date[6:]
    return f"{yyyy}/{mm}/{dd}"