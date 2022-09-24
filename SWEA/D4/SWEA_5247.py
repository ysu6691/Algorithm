testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    num_list = [[N]]
    memo = {N}

    cnt = 1

    while True:
        num_list.append([])
        for num in num_list[cnt-1]:
            if num + 1 not in memo and num + 1 <= 1000000:
                num_list[cnt].append(num+1)
                memo.add(num+1)
            if num - 1 not in memo and num - 1 <= 1000000:
                num_list[cnt].append(num-1)
                memo.add(num-1)
            if num * 2 not in memo and num * 2 <= 1000000:
                num_list[cnt].append(num*2)
                memo.add(num*2)
            if num - 10 not in memo and num - 10 <= 1000000:
                num_list[cnt].append(num-10)
                memo.add(num-10)

        if M in num_list[cnt]:
            break

        cnt += 1

    print(f'#{tc} {cnt}')