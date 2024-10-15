def is_student_id(string):
    con_len = len(string)==8
    con_1ch = string[0] in 'rsRS'
    con_digits = string[1:].isdigit()
    return con_len and con_1ch and con_digits