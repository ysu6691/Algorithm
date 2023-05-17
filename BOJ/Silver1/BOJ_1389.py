import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 987654321
distance = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    distance[i][i] = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    distance[n1][n2] = 1
    distance[n2][n1] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])

min_acc = INF
answer = 0
for n in range(1, N + 1):
    if sum(distance[n][1:]) < min_acc:
        answer = n
        min_acc = sum(distance[n][1:])

print(answer)
