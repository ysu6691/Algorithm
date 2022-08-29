testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0

    dx1 = [-1, 1, 0, 0]
    dy1 = [0, 0, -1, 1]

    dx2 = [-1, 1, -1, 1]
    dy2 = [1, -1, -1, 1]

    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]
            cnt2 = arr[i][j]

            for p in range(1, M):
                for q in range(4):
                    nx1 = dx1[q]*p + j
                    ny1 = dy1[q]*p + i

                    nx2 = dx2[q]*p + j
                    ny2 = dy2[q]*p + i

                    if 0 <= nx1 < N and 0 <= ny1 < N:
                        cnt1 += arr[ny1][nx1]
                    if 0 <= nx2 < N and 0 <= ny2 < N:
                        cnt2 += arr[ny2][nx2]

            if cnt1 > max_cnt:
                max_cnt = cnt1
            if cnt2 > max_cnt:
                max_cnt = cnt2

    print(f'#{tc} {max_cnt}')
