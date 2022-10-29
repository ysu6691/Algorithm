from copy import deepcopy

# 상어가 이동하는 64가지 경우 생성
def makeSharkDirection(depth):
    if depth == 3:
        move_list.append(selection[:])
        return

    for i in range(4):
        selection[depth] = direction_list[i]
        makeSharkDirection(depth+1)


# 물고기 움직이기
def fishMove():
    # 새로운 배열에 저장하기
    new_arr = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for direction in range(8):
                # 해당 좌표에 해당 방향을 바라보는 물고기가 있다면,
                if arr[r][c][direction]:
                    num = arr[r][c][direction]
                    cnt = 0
                    # 방향 변경하면서 이동할 수 있으면 이동하기
                    while True:
                        nr = r + dr[direction]
                        nc = c + dc[direction]
                        if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark_r, shark_c) and not fish_smell[nr][nc]:
                            new_arr[nr][nc][direction] += num
                            break
                        direction -= 1
                        if direction == -1:
                            direction = 7
                        cnt += 1
                        # 이동할 수 없다면, 원래 위치와 방향 그대로
                        if cnt == 8:
                            new_arr[r][c][direction] += num
                            break
    return new_arr


# 상어 움직이기
def sharkMove():
    max_cnt = -1
    # 64가지 방향 중 가장 먼저 움직일 수 있는 방향으로 이동
    for move in move_list:
        cnt = 0
        flag = False
        nr = shark_r
        nc = shark_c
        visited = set()
        path = set()
        for direction in move:
            nr += dr[direction]
            nc += dc[direction]
            path.add((nr, nc))
            # 배열 벗어나면 다음 방향 보기
            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                flag = True
                break
            # 이미 방문한 곳을 또 방문할 수 있으므로, 이미 방문한 곳의 물고기 수는 세지 않기
            if (nr, nc) not in visited:
                cnt += sum(arr[nr][nc])
                visited.add((nr, nc))

        # 이동할 수 있고 먹을 수 있는 물고기 수도 최대라면,
        # 그 때의 경로와 최종 위치 저장
        if not flag and cnt > max_cnt:
            max_cnt = cnt
            max_nr = nr
            max_nc = nc
            max_path = set(path)

    # 저장한 경로대로 움직이면서 물고기 없애고 냄새 남기기
    for position in max_path:
        for direction in range(8):
            if arr[position[0]][position[1]][direction]:
                fish_smell[position[0]][position[1]] = 3
                arr[position[0]][position[1]][direction] = 0

    return max_nr, max_nc


# 냄새 1씩 줄이기
def reduceSmell():
    for r in range(4):
        for c in range(4):
            if fish_smell[r][c]:
                fish_smell[r][c] -= 1


# 물고기 복사
def copyFishes():
    for r in range(4):
        for c in range(4):
            for direction in range(8):
                arr[r][c][direction] += original_arr[r][c][direction]

##############################################################################

M, S = map(int, input().split())
# 8개의 방향 중, 각 방향을 보는 물고기가 몇 마리 있는지 나타냄
# arr[r][c] = [0, 0, 0, 0, 0, 0, 0, 0]
arr = [[[0]*8 for _ in range(4)] for _ in range(4)]
fish_smell = [[0]*4 for _ in range(4)]
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    r, c, d = map(int, input().split())
    arr[r-1][c-1][d-1] += 1

shark_r, shark_c = map(int, input().split())
shark_r -= 1
shark_c -= 1

# 상어 이동 중복 순열 생성
move_list = []
direction_list = [2, 0, 6, 4]
selection = [0] * 3
makeSharkDirection(0)

# 시뮬레이션 시작
for _ in range(S):
    # 원래 물고기 위치 기억
    original_arr = deepcopy(arr)
    arr = fishMove() # 물고기 이동
    shark_r, shark_c = sharkMove() # 상어 이동
    reduceSmell() # 냄새 줄이기
    copyFishes() # 원래 물고기 복사


answer = 0
for r in range(4):
    for c in range(4):
        answer += sum(arr[r][c])

print(answer)

