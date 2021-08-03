from random import choice

from constants import PLAYER_OPTIONS, RESULT_BANNER, CONTROL_OPTIONS
from core import chek_one_hand, modify_scores, check_total

scores = {
    'user': 0, 'system': 0,
    'total_user': 0, 'total_system': 0
}
play = True
while play:

    user_input = input("enter your choice please:")
    system_choice = choice(list(PLAYER_OPTIONS.keys()))

    if user_input in PLAYER_OPTIONS.keys():
        result = chek_one_hand(user_input, system_choice)
        scores = modify_scores(result, scores)
        scores = check_total(scores)

        print(PLAYER_OPTIONS[user_input], PLAYER_OPTIONS[system_choice],
              '\n' + RESULT_BANNER[result]
              )

    elif user_input in CONTROL_OPTIONS.keys():
        play = False
        print('Bye')

    else:
        print('try again ')
