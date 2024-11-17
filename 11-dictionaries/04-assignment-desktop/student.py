def desktop(catalog, components):
    sum = 0
    for component in components:
        sum += catalog[component]
    return sum