testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    num_list = [0, 1, 1, 1, 2, 2]

    if N < 6:
        result = num_list[N]
    else:
        for i in range(6, N+1):
            num_list.append(num_list[i-1] + num_list[i-5])
        result = num_list[N]

    print(f'#{tc} {result}')
