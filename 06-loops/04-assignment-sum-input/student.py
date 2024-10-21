def sum_input():
    number = int(input("Enter integer: "))
    sum = 0
    while number != 0:
        sum += number
        number = int(input("Enter integer: "))
    print(f"The sum equals {sum}.")

# a = sum_input()