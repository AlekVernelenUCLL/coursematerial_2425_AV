def sell(stock, model):
    if stock[model] == 1:
        del stock[model]
    else:
        stock[model] -= 1
    return stock

# stock = {
#     'New Balance 530': 5,
#     'Converse Chuck Taylor All Star 70 Hi': 2,
#     'Air Jordan 1 Retro': 8,
#     'Nike Air Max Tuned 1': 1,
#     'Adidas Superstar': 4,
#     'Vans Classic Slip-on Checkered': 15
# }

# print(sell(stock,"New Balance 530"))