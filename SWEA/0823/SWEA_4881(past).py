testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    selection = [0] * N

    result = []

    min_sum = 9 * N

    def perm(depth, sum_num):
        global min_sum
        if depth == N:
            if sum(selection) < min_sum:
                min_sum = sum(selection)

            return

        for i in range(N):
            n = sum_num
            if not check[i]:
                check[i] = 1
                selection[depth] = arr[depth][i]
                n += selection[depth]
                if n >= min_sum:
                    check[i] = 0
                    continue
                perm(depth + 1, n)
                check[i] = 0

    perm(0, 0)

    print(f'#{tc} {min_sum}')

