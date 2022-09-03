# 

N = int(input())

dice_list = [list(map(int, input().split())) for _ in range(N)]

opposite_list = [5, 3, 4, 1, 2, 0]

max_cnt = 0

for i in range(6):
    cnt = 0
    top = dice_list[0][i]

    for dice in dice_list:

        for j in range(6):
            if dice[j] == top:
                except_number = [top, dice[opposite_list[j]]]
                top = dice[opposite_list[j]]
                break

        max_num = 0

        for j in range(6):
            if dice[j] not in except_number:
                if dice[j] > max_num:
                    max_num = dice[j]

        cnt += max_num

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
