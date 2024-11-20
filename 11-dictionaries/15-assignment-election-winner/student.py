def election_winner(votes):
    if votes:
        results = dict()
        for vote in votes:
            if results.setdefault(vote, 0) > -1:
                results[vote] += 1
        maximum = 0
        for person, value in results.items():
            if value > maximum:
                maximum = value
                winner = person
        return winner
    return None