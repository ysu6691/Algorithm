import sys
input = sys.stdin.readline

T, W = map(int, input().split())
dp = [[[0, 0] for i in range(W + 1)] for j in range(T)]
nums = [int(input()) for _ in range(T)]

acc = 0
for i in range(T):
    if nums[i] == 1:
        acc += 1
    dp[i][0][0] = acc

for i in range(W + 1):
    if nums[0] == 1 and not i % 2:
        dp[0][i][0] = 1
    elif nums[0] == 2 and i % 2:
        dp[0][i][1] = 1

for c in range(1, W + 1):
    for r in range(1, T):
        if nums[r] == 1:
            dp[r][c][0] = max(dp[r - 1][c][0], dp[r - 1][c - 1][1]) + 1
            dp[r][c][1] = max(dp[r - 1][c][1], dp[r - 1][c - 1][0])
        else:
            dp[r][c][0] = max(dp[r - 1][c][0], dp[r - 1][c - 1][1])
            dp[r][c][1] = max(dp[r - 1][c][1], dp[r - 1][c - 1][0]) + 1

answer = 0
for i in range(W + 1):
    answer = max(max(dp[-1][i]), answer)

print(answer)