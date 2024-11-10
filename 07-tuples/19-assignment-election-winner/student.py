def election_winner(votes):
    if not votes:
        return None
    votes_sorted = sorted(votes)
    first = votes_sorted[0]
    count = 0
    i = 0
    index = (0,)
    votes_total = ()
    for vote in votes_sorted:
        if vote == first:
            count += 1
        else:
            votes_total += (count,)
            index += (i,)
            count = 1
            first = votes_sorted[i]
        i += 1
    votes_total += (count,)
    votes_winner = max(votes_total)
    a = 0
    for element in votes_total:
        if element == votes_winner:
            index_winner = index[a]
            return votes_sorted[index_winner]
        a += 1

# print(election_winner(("bart","mano","luc","mano","luc","bart","mano","luc","mano")))