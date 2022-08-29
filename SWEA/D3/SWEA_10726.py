def binary(n):
    if n < 2:
        return str(n)

    if n % 2:
        return binary(n // 2) + '1'
    else:
        return binary(n // 2) + '0'

testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())

    binary_M = binary(M)

    for i in range(len(binary_M) - 1, len(binary_M) - N - 1, -1):
        if i < 0:
            result = 'OFF'
            break

        else:
            if binary_M[i] == '1':
                result = 'ON'
            else:
                result = 'OFF'
                break

    print(f'#{tc} {result}')