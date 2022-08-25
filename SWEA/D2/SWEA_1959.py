testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        long = N
        short = M
        long_num = A
        short_num = B
    else:
        long = M
        short = N
        long_num = B
        short_num = A

    max_acc = 0

    for i in range(long - short + 1):
        acc = 0

        for j in range(short):
            acc += long_num[i+j] * short_num[j]

        if acc > max_acc:
            max_acc = acc

    print(f'#{tc} {max_acc}')
