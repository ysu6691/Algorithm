testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [input() for _ in range(N)]

    di = [-1, 1, 1, -1]
    dj = [-1, 1, -1, 1]

    finish = False
    result = 'NO'

    for i in arr:
        if 'ooooo' in i:
            result = 'YES'
            finish = True

    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += arr[j][i]

        if 'ooooo' in tmp:
            result = 'YES'
            finish = True

    for i in range(N):
        for j in range(N):

            if arr[i][j] == 'o':

                for k in range(4):
                    cnt = 1
                    ni = i + di[k]
                    nj = j + dj[k]

                    while 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break

                        if cnt == 5:
                            result = 'YES'
                            finish = True
                            break

                        ni += di[k]
                        nj += dj[k]

                    if finish:
                        break

            if finish:
                break

        if finish:
            break

    print(f'#{tc} {result}')
