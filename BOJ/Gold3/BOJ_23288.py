from collections import deque

# 주사위 굴리기
def dice_move(r, c, direction):
    while True:
        nr = r + dr[direction]
        nc = c + dc[direction]
        if 0 <= nr < N and 0 <= nc < M:
            break
        if direction == 0:
            direction = 1
        elif direction == 1:
            direction = 0
        elif direction == 2:
            direction = 3
        elif direction == 3:
            direction = 2

    new_dice = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        new_dice[i] = dice[dice_dict[direction][i]]
    return nr, nc, new_dice, direction


# 점수 획득
def BFS(r, c):
    global answer

    queue = deque([(r, c)])
    visited = set()
    cnt = 0

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            cnt += 1
            for i in range(4):
                nr = current[0] + dr[i]
                nc = current[1] + dc[i]
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and arr[nr][nc] == arr[r][c]:
                    queue.append((nr, nc))

    answer += cnt * arr[r][c]


# 이동방향 결정
def change_direction(r, c, direction):
    if dice[5] > arr[r][c]:
        if direction == 0:
            direction = 3
        elif direction == 1:
            direction = 2
        elif direction == 2:
            direction = 0
        elif direction == 3:
            direction = 1

    elif dice[5] < arr[r][c]:
        if direction == 0:
            direction = 2
        elif direction == 1:
            direction = 3
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 0

    return direction


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

r = 0
c = 0
# 상, 북, 동, 서, 남, 하
dice = [1, 2, 3, 4, 5, 6]

# 0: 동, 1: 서, 2: 북, 3: 남
dice_dict = {0: [3, 1, 0, 5, 4, 2],
             1: [2, 1, 5, 0, 4, 3],
             2: [4, 0, 2, 3, 5, 1],
             3: [1, 5, 2, 3, 0, 4]}

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
direction = 0

answer = 0

for _ in range(K):
    r, c, dice, direction = dice_move(r, c, direction)
    BFS(r, c)
    direction = change_direction(r, c, direction)

print(answer)