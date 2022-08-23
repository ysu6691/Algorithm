def perm(depth, acc):
    global min_num
    if acc > min_num:
        return

    if depth == N:
        min_num = acc

    for i in range(N):
        if not check[i]:
            check[i] = 1
            perm(depth+1, acc + arr[depth][i])
            check[i] = 0

testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    min_num = 1500

    perm(0, 0)

    print(f'#{tc} {min_num}')