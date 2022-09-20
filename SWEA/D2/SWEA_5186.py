# 2진법으로 변환
def binaryTransform(n, digit, result):
    if n == 0 and digit <= 12:
        return result
    elif digit > 12:
        return 'overflow'

    # ex1) n = 0.15, digit = 2
    #      2^(-3) = 0.125, 2^(-2) = 0.25
    #      0.125 <= n < 0.25 이므로,
    #      0.15 - 0.125 = 0.025가 다음 재귀로 들어간다 (1을 남기고)

    # ex2) n = 0.15, digit = 1
    #      2^(-2) = 0.25, 2^(-1) = 0.5
    #      n < 0.25 이므로,
    #      0.25 그대로 다음 재귀로 들어간다 (0을 남기고)

    if 2 ** -(digit+1) <= n < 2 ** -digit:
        return binaryTransform(n - 2 ** -(digit+1), digit+1, result + '1')
    else:
        return binaryTransform(n, digit+1, result + '0')


testcase = int(input())

for tc in range(1, testcase+1):
    N = float(input())
    print(f"#{tc} {binaryTransform(N, 0, '')}")