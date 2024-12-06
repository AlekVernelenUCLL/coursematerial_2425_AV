def remove_empty_lines(source, destination):
    with open(source, 'r', encoding='utf-8') as file1:
        lines = file1.readlines()
            
    with open(destination, 'a', encoding='utf)8') as file2:
        for line in lines:
            