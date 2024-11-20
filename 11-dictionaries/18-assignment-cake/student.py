def cake(stock, recipe_ingredients):
    result = []
    for ingr, amount in recipe_ingredients.items():
        cakes = stock.setdefault(ingr,0) // amount
        result.append(cakes)
    return min(result)

stock = {
    "sugar": 1500,
    "eggs": 20,
    "flour": 2000,
    "butter": 1000,
    "chocolate": 2500,
    "salt": 250
}

cake_ingredients = {
    "butter": 250,
    "eggs": 4,
    "flour": 250,
    "sugar": 250
}