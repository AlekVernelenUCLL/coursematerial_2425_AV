def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0
    elif player1_choice == 0:
        return 1
    elif player2_choice == 0:
        return 2
    elif player1_choice > player2_choice:
        return 1
    elif player2_choice > player1_choice:
        return 2