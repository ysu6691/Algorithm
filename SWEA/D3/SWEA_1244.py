def calc(cnt):
    if cnt == C:
        if N_list not in calc_list:
            calc_list.append(N_list[:])
        return

    for i in range(length - 1):
        for j in range(i+1, length):
            N_list[i], N_list[j] = N_list[j], N_list[i]
            calc(cnt+1)
            N_list[i], N_list[j] = N_list[j], N_list[i]


testcase = int(input())

for tc in range(1, testcase+1):
    N, change = input().split()

    N_list = list(N)
    sorted_list = sorted(N_list)
    C = int(change)
    if C == 6 or C == 8 or C == 10:
        C = 4
    elif C == 7 or C == 9:
        C = 5
    length = len(N_list)

    calc_list = []
    calc(0)

    num_list = []

    for i in calc_list:
        num = ''
        for j in range(length):
            num += i[j]
        num_list.append(int(num))

    result = sorted(num_list)[-1]
    print(f'#{tc} {result}')
