from collections import deque, defaultdict

testcase = int(input())

for tc in range(1, testcase+1):
    N, M, K, A, B = map(int, input().split())
    reception_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    customer_arrive = list(map(int, input().split()))
    customer_arrive = deque(customer_arrive)

    reception_desk = [[0, 0] for _ in range(N)]
    repair_desk = [[0, 0] for _ in range(M)]
    reception_wait = deque()
    repair_wait = deque()
    customer_memo = defaultdict(list)

    time = 0
    customer_num = 1

    while True:
        # 고객 정비소 도착
        if customer_arrive:
            while customer_arrive[0] == time:
                reception_wait.append(customer_num)
                customer_num += 1
                customer_arrive.popleft()
                if not customer_arrive:
                    break

        # print('정비 전 reception_wait: ', reception_wait)
        # print('정비 전 repair_desk: ', repair_desk)

        # 정비하기
        for i in range(M):
            if repair_desk[i][1]:
                repair_desk[i][1] -= 1

        # print('정비 후 repair_desk: ', repair_desk)

        # 정비하러 입장
        if repair_wait:
            memo = deque()
            for i in range(M):
                if not repair_desk[i][1]:
                    memo.append(i)
                    if len(memo) == len(repair_wait):
                        break
            while repair_wait and memo:
                customer = repair_wait.popleft()
                num = memo.popleft()
                repair_desk[num] = [customer, repair_time[num]]
                customer_memo[customer].append(num+1)

        # print('정비 입장 후 repair_desk: ', repair_desk)
        # print('정비 입장 후 customer_memo: ', customer_memo)
        #
        # print('접수 전 reception_desk: ', reception_desk)
        # print('접수 전 repair_wait :', repair_wait)

        # 접수하기
        for i in range(N):
            if reception_desk[i][1]:
                reception_desk[i][1] -= 1
                if reception_desk[i][1] == 0:
                    repair_wait.append(reception_desk[i][0])

        # print('접수 후 reception_desk :', reception_desk)
        # print('접수 후 repair_wait :', repair_wait)

        # 접수하러 입장
        if reception_wait:
            memo = deque()
            for i in range(N):
                if not reception_desk[i][1]:
                    memo.append(i)
                    if len(memo) == len(reception_wait):
                        break
            while reception_wait and memo:
                customer = reception_wait.popleft()
                num = memo.popleft()
                reception_desk[num] = [customer, reception_time[num]]
                customer_memo[customer].append(num+1)

        # print('접수 입장 후 reception_desk :', reception_desk)
        # print('접수 입장 후 customer_memo :', customer_memo)

        time += 1
        # print(time)

        flag1 = False
        for i in range(N):
            if reception_desk[i][1]:
                break
        else:
            flag1 = True

        flag2 = False
        for i in range(M):
            if repair_desk[i][1]:
                break
        else:
            flag2 = True

        if not customer_arrive and flag1 and flag2:
            break

    answer = 0
    for i in range(1, K + 1):
        if customer_memo[i] == [A, B]:
            answer += i
    if not answer:
        answer = -1
    print(f'#{tc} {answer}')

