def box(string):
    above_under = '+'+((len(string)+2)*'-')+'+'
    return f"{above_under}\n| {string} |\n{above_under}"