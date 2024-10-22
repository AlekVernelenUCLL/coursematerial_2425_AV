def remove_double_spaces(text):
    for char in text:
        if char == " ":
            count += 1
        else:
            if count > 1:
                
            else:
                s += char


a = "dit    is    een    voorbeeldtekst"
print(remove_double_spaces(a))