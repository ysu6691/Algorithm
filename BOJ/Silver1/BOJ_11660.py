import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0] * (N + 1)]
arr += [[0] + list(map(int, input().split())) for _ in range(N)]

for r in range(1, N + 1):
    for c in range(1, N + 1):
        arr[r][c] += arr[r][c - 1]

for c in range(1, N + 1):
    for r in range(1, N + 1):
        arr[r][c] += arr[r - 1][c]

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    sys.stdout.write(str(arr[r2][c2] - arr[r2][c1 - 1] - arr[r1 - 1][c2] + arr[r1 - 1][c1 - 1]) + "\n")
sys.stdout.flush()
