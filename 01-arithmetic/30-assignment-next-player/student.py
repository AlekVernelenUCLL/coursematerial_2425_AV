def next_player(player, player_count):
    next = player+1
    next_cycle = next%player_count
    return next_cycle