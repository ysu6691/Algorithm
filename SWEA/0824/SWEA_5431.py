testcase = int(input())

for tc in range(1, testcase+1):

    N, K = map(int, input().split())

    nums = list(map(int, input().split()))

    result = []

    for i in range(1, N+1):
        if i not in nums:
            result.append(i)

    result = ' '.join(map(str, result))

    print(f'#{tc} {result}')