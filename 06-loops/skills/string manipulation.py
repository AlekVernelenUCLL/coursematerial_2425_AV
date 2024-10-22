def remove_double_spaces(text):
    s = ""
    count = 0
    for char in text:
        if char == " ":
            count += 1
        elif count >= 1:
            s += " "+char
            count = 0
        else:
            s += char
    return f"'{s}'"



a = "   Deze tekst dient  als      voorbeeld  voor deze   oefening  "
print(remove_double_spaces(a))