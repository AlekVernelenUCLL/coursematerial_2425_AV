def rankings(participants):
    rankings = dict()
    num = 1
    for participant in participants:
        rankings[participant] = num
        num += 1
    return rankings

# a = [
# "Raymond Garraty",
# "Stebbins",
# "Peter McVries",
# "Arthur Baker",
# "Abraham",
# "Collie Parker"
# ]

# print(rankings(a))