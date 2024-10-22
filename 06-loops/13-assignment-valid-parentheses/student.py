def valid_parentheses(string):
    count = 0
    for char in string:
        if count == 0 and char == ")":
            return False
        elif char == "(":
            count += 1
        elif char == ")":
            count -=1
    return count == 0

# print(valid_parentheses("()()(()())"))