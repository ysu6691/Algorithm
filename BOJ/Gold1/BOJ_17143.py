# 낚시하기
def capture():
    global answer
    # 현재 열에서 행 올리면서 첫 상어 잡기
    for nr in range(R):
        if arr[nr][nc]:
            answer += arr[nr][nc][2]
            arr[nr][nc] = 0
            break


# 상어 이동하기
def move():
    # 이동한 상어 저장할 배열 생성
    new_arr = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c]:
                # 위 방향
                if arr[r][c][1] == 1:
                    if r - arr[r][c][0] >= 0:
                        new_r = r - arr[r][c][0]
                        if new_arr[new_r][c]:
                            if new_arr[new_r][c][2] < arr[r][c][2]:
                                new_arr[new_r][c] = arr[r][c]
                        else:
                            new_arr[new_r][c] = arr[r][c]
                    else:
                        s = arr[r][c][0] - r
                        if s // (R-1) % 2:
                            new_d = 1
                            new_r = R - 1 - (s % (R-1))
                        else:
                            new_d = 2
                            new_r = s % (R-1)
                        if new_arr[new_r][c]:
                            if new_arr[new_r][c][2] < arr[r][c][2]:
                                new_arr[new_r][c] = (arr[r][c][0], new_d, arr[r][c][2])
                        else:
                            new_arr[new_r][c] = (arr[r][c][0], new_d, arr[r][c][2])

                # 아래 방향
                elif arr[r][c][1] == 2:
                    if r + arr[r][c][0] < R:
                        new_r = r + arr[r][c][0]
                        if new_arr[new_r][c]:
                            if new_arr[new_r][c][2] < arr[r][c][2]:
                                new_arr[new_r][c] = arr[r][c]
                        else:
                            new_arr[new_r][c] = arr[r][c]
                    else:
                        s = arr[r][c][0] - (R - 1 - r)
                        if (s // (R-1)) % 2 == 0:
                            new_d = 1
                            new_r = R - 1 - (s % (R-1))
                        else:
                            new_d = 2
                            new_r = s % (R-1)
                        if new_arr[new_r][c]:
                            if new_arr[new_r][c][2] < arr[r][c][2]:
                                new_arr[new_r][c] = (arr[r][c][0], new_d, arr[r][c][2])
                        else:
                            new_arr[new_r][c] = (arr[r][c][0], new_d, arr[r][c][2])

                # 오른쪽 방향
                elif arr[r][c][1] == 3:
                    if c + arr[r][c][0] < C:
                        new_c = c + arr[r][c][0]
                        if new_arr[r][new_c]:
                            if new_arr[r][new_c][2] < arr[r][c][2]:
                                new_arr[r][new_c] = arr[r][c]
                        else:
                            new_arr[r][new_c] = arr[r][c]
                    else:
                        s = arr[r][c][0] - (C - 1 - c)
                        if s // (C-1) % 2 == 0:
                            new_d = 4
                            new_c = C - 1 - (s % (C-1))
                        else:
                            new_d = 3
                            new_c = s % (C-1)
                        if new_arr[r][new_c]:
                            if new_arr[r][new_c][2] < arr[r][c][2]:
                                new_arr[r][new_c] = (arr[r][c][0], new_d, arr[r][c][2])
                        else:
                            new_arr[r][new_c] = (arr[r][c][0], new_d, arr[r][c][2])

                # 왼쪽 방향
                elif arr[r][c][1] == 4:
                    if c - arr[r][c][0] >= 0:
                        new_c = c - arr[r][c][0]
                        if new_arr[r][new_c]:
                            if new_arr[r][new_c][2] < arr[r][c][2]:
                                new_arr[r][new_c] = arr[r][c]
                        else:
                            new_arr[r][new_c] = arr[r][c]
                    else:
                        s = arr[r][c][0] - c
                        if s // (C-1) % 2:
                            new_d = 4
                            new_c = C - 1 - (s % (C-1))
                        else:
                            new_d = 3
                            new_c = s % (C-1)
                        if new_arr[r][new_c]:
                            if new_arr[r][new_c][2] < arr[r][c][2]:
                                new_arr[r][new_c] = (arr[r][c][0], new_d, arr[r][c][2])
                        else:
                            new_arr[r][new_c] = (arr[r][c][0], new_d, arr[r][c][2])

    return new_arr


R, C, M = map(int, input().split())
arr = [[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = (s, d, z)

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

nc = -1
answer = 0

for _ in range(C):
    nc += 1
    capture()
    arr = move()

print(answer)
