# def remove_backspaces(string):
#     s = ""
#     count = 0
#     i = 0
#     for char in string:
#         i += 1
#         if char == "\\":
#             count += 1
#         elif count == 1 and char == "b":
#             s -= string[i]
#             count = 0
#         elif count == 0:
#             s += char

def remove_backspaces(string):
    count = 0
    s = ""
    i = 0
    for char in string:
        i += 1
        if count == 1 and char == "\\":
            s -= string[i-2]
        