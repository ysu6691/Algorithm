testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    idx_list = [[N//2]]

    n = 1

    while n <= N//2:
        left = N // 2 - n
        right = N // 2 + n

        idx_list.append(list(range(left, right+1)))

        n += 1

    for i in range(N//2):
        idx_list.append(idx_list[N//2 - i - 1])

    cnt = 0

    for i in range(N):
        for j in idx_list[i]:
            cnt += arr[i][j]

    print(f'#{tc} {cnt}')