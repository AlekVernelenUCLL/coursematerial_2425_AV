athletes = (
    ("Lisa De Vries", 12.84),
    ("James Thompson", 13.21),
    ("Sophie Dubois", 12.75),
    ("Thomoya Sato", 12.90),
    ("Marta Rossi", 12.88),
    ("Jules Francois", 13.13)
)

def get_name(athletes):
    for athlete in athletes:
        print(athlete[0])

get_name(athletes)