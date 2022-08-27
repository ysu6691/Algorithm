testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())

    tk_list = [int(input()) for _ in range(N)]

    min_time = 0
    max_time = min(tk_list) * M

    acc = 0

    while min_time <= max_time:
        guess_time = (max_time + min_time) // 2
        acc = 0

        for tk in tk_list:
            acc += guess_time // tk

            if acc >= M:
                ans = guess_time
                max_time = guess_time - 1
                break

        if acc < M:
            min_time = guess_time + 1

    print(f'#{tc} {ans}')