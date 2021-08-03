from constants import PLAY_RULE


def chek_one_hand(user_choice, system_choice):
    return PLAY_RULE[user_choice][system_choice]


def modify_scores(curren_result, current_scores):
    if curren_result == 1:
        current_scores['user'] += 1
    elif curren_result == -1:
        current_scores['system'] += 1
    return current_scores


def check_total(curren_scores):
    if curren_scores['user'] == 3:
        curren_scores['total_user'] += 1
        curren_scores['user'] = 0
        curren_scores['system'] = 0
        print('#' * 30, '\tyou win\t', '#' * 30)
    elif curren_scores['system'] == 3:
        curren_scores['total_system'] += 1
        curren_scores['user'] = 0
        curren_scores['system'] = 0
        print('#' * 30, '\tyou lose\t', '#' * 30)
    return curren_scores
