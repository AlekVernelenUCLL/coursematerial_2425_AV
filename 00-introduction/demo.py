number = int(input("type a number: "))
def multiply_by_then(number):
    result = number*10
    return result

def subtract_by_five(number):
    result = multiply_by_then(number)-5
    return result



print(subtract_by_five(number))
print(number*10-5)