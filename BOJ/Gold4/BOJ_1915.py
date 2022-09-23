n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]

max_width = 0

for i in range(n):
    if arr[i][0]:
        max_width = 1
for i in range(m):
    if arr[0][i]:
        max_width = 1

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j]:
            arr[i][j] += min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
            if arr[i][j] > max_width:
                max_width = arr[i][j]

print(max_width ** 2)
