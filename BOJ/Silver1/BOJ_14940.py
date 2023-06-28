import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
flag = False
for r in range(n):
    for c in range(m):
        if arr[r][c] == 2:
            queue.append((r, c, 0))
            flag = True
            break
    if flag:
        break

answer = [[0] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while queue:
    r, c, cnt = queue.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not answer[nr][nc] and arr[nr][nc] == 1:
            answer[nr][nc] = cnt + 1
            queue.append((nr, nc, cnt + 1))

for r in range(n):
    for c in range(m):
        if not answer[r][c] and arr[r][c] == 1:
            answer[r][c] = -1

for r in range(n):
    print(" ".join(map(str, answer[r])))
