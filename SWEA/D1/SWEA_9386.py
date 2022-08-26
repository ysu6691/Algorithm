testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    char = input()

    max_cnt = 0
    cnt = 0

    for i in range(N):
        if char[i] == '1':
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 0

    if cnt > max_cnt:
        max_cnt = cnt
        cnt = 0

    print(f'#{tc} {max_cnt}')