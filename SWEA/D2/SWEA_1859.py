testcase = int(input())
for tc in range(1, testcase+1):
    n = int(input())
    items = list(map(int, input().split()))

    max_cost = items[-1] # 가장 큰 값은 먼저 맨 뒤에 값으로 설정
    profit = 0

    for i in range(n - 2, -1 , -1): # 뒤에서부터 탐색
        if items[i] >= max_cost: # 만약 가장 큰 값보다 크다면,
            max_cost = items[i] # 갱신
        else: # 더 작은 값을 만나면,
            profit += max_cost - items[i] # 차이 누적

    print(f'#{tc} {profit}')