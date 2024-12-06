filename = 'books.txt'

with open(filename, "r", encoding="utf-8") as file:
    list_lines = file.readlines()
print(list_lines)
