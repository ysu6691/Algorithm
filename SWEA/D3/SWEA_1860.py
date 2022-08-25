testcase = int(input())

for tc in range(1, testcase+1):

    N, M, K = map(int, input().split())

    customer = list(map(int, input().split()))
    customer.sort()

    item = 0
    second = 0
    result = 'Possible'
    finish = False

    while customer:
        while second == customer[0]:
            if item >= 1:
                item -= 1
                customer.pop(0)
                if not customer:
                    finish = True
                    break
            else:
                result = 'Impossible'
                finish = True
                break

        second += 1
        if not (second % M):
            item += K

        if finish:
            break

    print(f'#{tc} {result}')
