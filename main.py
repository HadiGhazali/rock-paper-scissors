from random import choice
from constants import PLAYER_OPTIONS, PLAY_BUTTON, STATUS
from core import check_win, modify_scores, check_total

scores = {'user': 0, 'system': 0, 'total_user': 0, 'total_system': 0}
play = True
while play:
    user_input = input('Enter your choice pleas')
    system_input = choice(list(PLAYER_OPTIONS.keys()))
    if user_input in PLAYER_OPTIONS.keys():
        result = check_win(user_input, system_input)
        current_scores = modify_scores(result, scores)
        print('your choice:{}, system choice:{},result:{},\t {}-{}'.format(PLAYER_OPTIONS[user_input],
                                                                           PLAYER_OPTIONS[system_input], STATUS[result],
                                                                           current_scores['user'],
                                                                           current_scores['system']))
        check_total(current_scores)

    elif user_input in PLAY_BUTTON.keys():
        play = False
        print('Bye!')
    else:
        print('Invalid input')
