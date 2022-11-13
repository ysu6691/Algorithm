def throw_dice(direction):
    new_dice = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        new_dice[i] = dice[throw_dict[direction][i]]
    return new_dice

########################################################

N, M, y, x, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

# 상, 북, 동, 서, 남, 하
dice = [0, 0, 0, 0, 0, 0]

# key: 방향 / value: [상, 북, 동, 서, 남, 하]
throw_dict = {1: [3, 1, 0, 5, 4, 2],
              2: [2, 1, 5, 0, 4, 3],
              3: [4, 0, 2, 3, 5, 1],
              4: [1, 5, 2, 3, 0, 4]}

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

for direction in move:
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 배열 벗어나면 무시
    if 0 <= nx < M and 0 <= ny < N:
        x = nx
        y = ny

        # 주사위 굴리기
        dice = throw_dice(direction)
        # 번호 교체
        if arr[y][x]:
            dice[5] = arr[y][x]
            arr[y][x] = 0
        else:
            arr[y][x] = dice[5]
        print(dice[0])