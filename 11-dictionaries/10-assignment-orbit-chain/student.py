def orbit_chain(orbits, start):
    lst = []
    while start in orbits:
        lst.append(start)
        start = orbits[start]
    lst.append(start)
    return lst

# orbits = {
#         'Moon': 'Earth',
#         'Mars': 'Sun',
#         'Earth': 'Sun',
#         'Jupiter': 'Sun',
#         'Saturn': 'Sun',
#         'Sun': 'Sagittarius A*',
#         'Phobos': 'Mars',
#         'Ganymede': 'Jupiter',
#         'Callisto': 'Jupiter',
#         'Europa': 'Jupiter',
#     }

# print(orbit_chain(orbits, "Moon"))