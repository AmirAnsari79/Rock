PLAYER_OPTIONS = \
    {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }
CONTROL_OPTIONS={'e':'EXIT'}
PLAY_RULE = {
    'r': {'r': 0, 'p': -1, 's': 1},
    's': {'r': -1, 'p': 1, 's': 0},
    'p': {'r': 1, 'p': 0, 's': -1},
}
RESULT_BANNER = {
    1: 'you win',
    -1: 'you lose',
    0: 'darws',
}
