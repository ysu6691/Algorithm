testcase = int(input())

binary_list = [2**i for i in range(31)]
result = []

for tc in range(1, testcase+1):
    N, V = map(int, input().split())
    cnt = 0

    check_N = False
    check_V = False

    for i in range(31):
        if binary_list[i] <= N < binary_list[i] + (binary_list[i] // 2):
            check_N = True
        if binary_list[i] <= V < binary_list[i] + (binary_list[i] // 2):
            check_V = True

    if check_N and check_V:
        cnt -= 1

    while N > 1:
        N //= 2
        cnt += 1

    while V > 1:
        V //= 2
        cnt += 1

    result.append(f'#{tc} {cnt}')

for i in range(len(result)):
    print(result[i])
