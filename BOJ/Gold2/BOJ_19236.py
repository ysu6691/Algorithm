from copy import deepcopy

# 상어 움직이기
def move(fishes, r, c, d, cnt, ate):
    global answer

    # 배열 벗어나면 최대값인지 확인
    if r < 0 or r >= 4 or c < 0 or c >= 4:
        if cnt > answer:
            answer = cnt
        return

    # 셋 id 분기
    ate = set(ate)

    # 처음 시작할 때는 먹고 이동하기
    if cnt != 0:
        nr = r + dr[d]
        nc = c + dc[d]
        # 안 먹고 상어 이동
        move(fishes, nr, nc, d, cnt, ate)

    # 빈 칸이라면 먹지 않고 넘어가기
    if fishes[r][c][0] in ate:
        return

    cnt += fishes[r][c][0] # 물고기 수 누적
    ate.add(fishes[r][c][0]) # 먹은 물고기 기억하기
    nd = fishes[r][c][1] # 방향 바꾸기
    nr = r + dr[nd]
    nc = c + dc[nd]

    # 물고기 이동
    new_fishes = fish_move(fishes, (r, c), ate)

    # 먹고 상어 이동
    move(new_fishes, nr, nc, nd, cnt, ate)


# 물고기 이동
def fish_move(arr, shark_position, ate):
    tmp_arr = deepcopy(arr)
    fish_dict = dict()
    # 물고기 번호에 맞는 좌표 및 방향 저장
    for i in range(4):
        for j in range(4):
            fish_dict[arr[i][j][0]] = [i, j, arr[i][j][1]]

    # 1번 물고기부터 이동
    for fish in range(1, 17):
        # 빈 칸이라면 continue
        if fish in ate:
            continue
        r = fish_dict[fish][0]
        c = fish_dict[fish][1]
        d = fish_dict[fish][2]
        # 방향 바꾸면서 갈 수 있는지 확인
        for i in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            # 갈 수 있으면 이동
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != shark_position:
                tmp_arr[r][c], tmp_arr[nr][nc] = tmp_arr[nr][nc], tmp_arr[r][c]
                tmp_arr[nr][nc][1] = d # 바뀐 방향 저장
                fish_dict[fish][2] = d # 바뀐 방향 저장
                fish_dict[fish][0], fish_dict[fish][1], fish_dict[tmp_arr[r][c][0]][0], fish_dict[tmp_arr[r][c][0]][1] = \
                    fish_dict[tmp_arr[r][c][0]][0], fish_dict[tmp_arr[r][c][0]][1], fish_dict[fish][0], fish_dict[fish][1]
                break
            else:
                d += 1
                if d == 9:
                    d = 1

    return tmp_arr

###################################################################

fishes = [[[0, 0]] * 4 for _ in range(4)]
row = 0
for _ in range(4):
    input_data = list(map(int, input().split()))
    for i in range(4):
        fishes[row][i] = [input_data[i*2], input_data[i*2+1]]
    row += 1

dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
first_direction = fishes[0][0][1]
ate = set()

move(fishes, 0, 0, first_direction, 0, ate)

print(answer)