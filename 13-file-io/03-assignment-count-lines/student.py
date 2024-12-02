def count_lines_in_file(path):
    with open(path, encoding='utf-8') as file:
        list = file.readlines()
        count = 0
        for line in list:
            count += 1
        return count