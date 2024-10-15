def tip_calculator():
    total_price = int(input("Enter total price: "))
    tip_percentage = input("Enter tip percentage: ")
    if not bool(tip_percentage):
        tip_percentage = 20
    result = total_price*(1+(int(tip_percentage)/100))
    print(f"You have to pay {round(result)}")