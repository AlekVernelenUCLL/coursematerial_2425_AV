def palindrome(string):
    forward = string
    backward = string[::-1]
    return forward == backward