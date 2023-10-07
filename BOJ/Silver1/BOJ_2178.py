import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque([(0, 0, 1)])
visited = {(0, 0)}

while queue:
    current = queue.popleft()

    if current[:2] == (N - 1, M - 1):
        print(current[2])
        break

    for i in range(4):
        nr = current[0] + dr[i]
        nc = current[1] + dc[i]
        if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and arr[nr][nc]:
            queue.append((nr, nc, current[2] + 1))
            visited.add((nr, nc))
