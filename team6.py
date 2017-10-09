


team_name = 'Team 6' 
strategy_name = 'If colluded against betray'
strategy_description = 'If colluded against it betrays '
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history)==0:
        return 'b'
    else:
        if 'c' in their_history:
            return 'b'
