def comb(idx, sidx):
    if sidx == 2:
        comb_list.append(selection[:])
        return

    if idx == N-1:
        return

    selection[sidx] = idx_list[idx]
    comb(idx+1, sidx+1)
    comb(idx+1, sidx)

testcase = int(input())

for tc in range(1, testcase+1):
    N, M = map(int, input().split())

    colors = [list(input()) for _ in range(N)]

    idx_list = list(range(1, N))
    selection = [0]*2
    comb_list = []

    comb(0, 0)
    min_cnt = N*M

    for i in comb_list:
        cnt = 0

        for j in range(N):
            for k in range(M):
                if j in range(0, i[0]):
                    if colors[j][k] != 'W':
                        cnt += 1

                elif j in range(i[0], i[1]):
                    if colors[j][k] != 'B':
                        cnt += 1

                elif j in range(i[1], N):
                    if colors[j][k] != 'R':
                        cnt += 1

        if cnt < min_cnt:
            min_cnt = cnt

    print(f'#{tc} {min_cnt}')
