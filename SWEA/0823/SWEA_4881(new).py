def perm(depth, acc):
    global min_sum
    if acc > min_sum:
        return
    
    elif depth == N:
        min_sum = acc
        return

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

    min_sum = 9 * N

    perm(0, 0)

    print(f'#{tc} {min_sum}')
