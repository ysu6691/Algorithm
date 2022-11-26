# 미세먼지 퍼뜨리기
def spread():
    # 새로운 2차원 배열 생성
    new_arr = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # 먼지가 있다면
            if arr[r][c] > 0:
                acc = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    # 좌표 안이고 공기청정기가 아니라면
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in purifiers:
                        new_arr[nr][nc] += arr[r][c] // 5 # 새로운 배열에 추가하기
                        acc += arr[r][c] // 5 # 추가한만큼 누적
                # 원래 위치에서 누적된 값만큼 빼서 옮기기
                new_arr[r][c] += arr[r][c] - acc
            # 공기청정기 위치 옮기기
            elif arr[r][c] == -1:
                new_arr[r][c] = -1
    return new_arr


# 공기 순환
def circulation():
    # 위쪽(반시계방향의 반대로 돌면서 숫자 옮기기)
    nr, nc = purifiers[0] # 위 공기청정기 좌표
    nr -= 1 # 바로 위 좌표 0으로
    arr[nr][nc] = 0
    # 위 방향
    while True:
        if nr - 1 == -1:
            break
        else:
            nr -= 1
            if arr[nr][nc] > 0:
                arr[nr + 1][nc] = arr[nr][nc]
                arr[nr][nc] = 0
    # 오른쪽 방향
    while True:
        if nc + 1 == C:
            break
        else:
            nc += 1
            if arr[nr][nc] > 0:
                arr[nr][nc - 1] = arr[nr][nc]
                arr[nr][nc] = 0
    # 아래 방향
    while True:
        if nr + 1 == purifiers[0][0] + 1:
            break
        else:
            nr += 1
            if arr[nr][nc] > 0:
                arr[nr - 1][nc] = arr[nr][nc]
                arr[nr][nc] = 0
    # 왼쪽 방향
    while True:
        if nc - 1 == 0:
            break
        else:
            nc -= 1
            if arr[nr][nc] > 0:
                arr[nr][nc + 1] = arr[nr][nc]
                arr[nr][nc] = 0

    # 아래 순환도 마찬가지로
    nr, nc = purifiers[1]
    nr += 1
    arr[nr][nc] = 0
    while True:
        if nr + 1 == R:
            break
        else:
            nr += 1
            if arr[nr][nc] > 0:
                arr[nr - 1][nc] = arr[nr][nc]
                arr[nr][nc] = 0

    while True:
        if nc + 1 == C:
            break
        else:
            nc += 1
            if arr[nr][nc] > 0:
                arr[nr][nc - 1] = arr[nr][nc]
                arr[nr][nc] = 0

    while True:
        if nr - 1 == purifiers[1][0] - 1:
            break
        else:
            nr -= 1
            if arr[nr][nc] > 0:
                arr[nr + 1][nc] = arr[nr][nc]
                arr[nr][nc] = 0

    while True:
        if nc - 1 == 0:
            break
        else:
            nc -= 1
            if arr[nr][nc] > 0:
                arr[nr][nc + 1] = arr[nr][nc]
                arr[nr][nc] = 0

############################################################

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
purifiers = []

for r in range(R):
    for c in range(C):
        if arr[r][c] == -1:
            purifiers.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    arr = spread()
    circulation()

# 정답 출력
answer = 2
for r in range(R):
    for c in range(C):
        answer += arr[r][c]

print(answer)