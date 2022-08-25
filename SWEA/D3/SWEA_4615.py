def change(x, y, color):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if arr[ny][nx] != color and arr[ny][nx] != 0:
            cnt = 0

            while 0 < nx <= N and 0 < ny <= N:

                if arr[ny][nx] == 0:
                    break

                elif arr[ny][nx] == color:
                    for j in range(cnt):
                        arr[y+dy[i]*(j+1)][x+dx[i]*(j+1)] = color
                    break

                else:
                    cnt += 1

                nx += dx[i]
                ny += dy[i]

testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())

    arr = [[0] * (N+2) for _ in range(N+2)]

    arr[N//2][N//2], arr[N//2+1][N//2+1] = 2, 2
    arr[N//2+1][N//2], arr[N//2][N//2+1] = 1, 1

    dx = [-1, 1, -1, 1, -1, 1, 0, 0]
    dy = [-1, 1, 1, -1, 0, 0, -1, 1]

    for i in range(M):
        x, y, color = map(int, input().split())
        arr[y][x] = color
        change(x, y, color)

    white = 0
    black = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    print(f'#{tc} {black} {white}')