def solution(lottos, win_nums):

    cnt = 0
    cnt_zero = 0

    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1
        elif lottos[i] == 0:
            cnt_zero += 1

    max_score = cnt + cnt_zero
    min_score = cnt

    score_dict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    answer = [score_dict[max_score], score_dict[min_score]]
    return answer