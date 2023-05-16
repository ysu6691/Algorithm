import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            queue.append((r, c, 0))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = -1
while queue:
    r, c, day = queue.popleft()
    if day > answer:
        answer = day

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            arr[nr][nc] = 1
            queue.append((nr, nc, day + 1))

for r in range(N):
    for c in range(M):
        if not arr[r][c]:
            answer = -1
            break
    if answer == -1:
        break

print(answer)
