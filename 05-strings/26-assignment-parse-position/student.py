def parse_position_x(string):
    indexcom = string.find(',')
    number = float(string[1:indexcom])
    if number == int(number):
        return int(number)
    return number

def parse_position_y(string):
    indexcom = string.find(',')
    number = float(string[indexcom+2:len(string)-1])
    if number == int(number):
        return int(number)
    return number

# c = "(12.000, 9.120)"
# a = parse_position_x(c)
# b = parse_position_y(c)
# print(a)
# print(b)