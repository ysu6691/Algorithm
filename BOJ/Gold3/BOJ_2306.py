import sys
input = sys.stdin.readline

def dfs(left, right):
    global answer

    if left >= right:
        return 0

    if memo[left][right] != -1:
        return memo[left][right]

    memo[left][right] = 0
    for i in range(left, right):
            memo[left][right] = max(dfs(left, i) + dfs(i + 1, right), memo[left][right])

    if (string[left] == "a" and string[right] == "t") or (string[left] == "g" and string[right] == "c"):
        memo[left][right] = max(dfs(left + 1, right - 1) + 2, memo[left][right])

    return memo[left][right]


string = input().rstrip()
N = len(string)
memo = [[-1] * N for _ in range(N)]
print(dfs(0, N - 1))

######################################

import sys
input = sys.stdin.readline

string = input().rstrip()
N = len(string)
dp = [[0] * N for _ in range(N)]

for size in range(1, N):
    for start in range(0, N - 1):
        end = start + size
        if end >= N:
            break
        if (string[start] == "a" and string[end] == "t") or (string[start] == "g" and string[end] == "c"):
            dp[start][end] = dp[start + 1][end - 1] + 2
        for mid in range(start, end):
            dp[start][end] = max(dp[start][mid] + dp[mid + 1][end], dp[start][end])

print(dp[0][-1])