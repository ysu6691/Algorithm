import sys
input = sys.stdin.readline

def multiply(arr1, arr2):
    new_arr = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            acc = 0
            for k in range(N):
                acc = (acc + arr1[r][k] * arr2[k][c]) % 1000
            new_arr[r][c] = acc
    return new_arr

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arrs = [arr]

for i in range(36):
    arrs.append(multiply(arrs[-1], arrs[-1]))

power = 36
answer = [[0] * N for _ in range(N)]
for i in range(N):
    answer[i][i] = 1

while power >= 0:
    if B >= 1 << power:
        answer = multiply(answer, arrs[power])
        B -= 1 << power
    power -= 1

for i in range(N):
    print(" ".join(map(str, answer[i])))
