PLAYER_OPTIONS = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
PLAY_BUTTON = {'e': 'Exit'}
PLAY_RULE = {
    'r': {'r': 0, 'p': -1, 's': 1},
    'p': {'r': 1, 'p': 0, 's': -1},
    's': {'r': -1, 'p': 1, 's': 0},

}

STATUS = {
    -1: 'you lose',
    0: 'draw',
    1: 'you win'
}
