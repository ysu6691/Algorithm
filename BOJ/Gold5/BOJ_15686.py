import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

total_home_cnt = 0
chicken_position = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            total_home_cnt += 1
        if arr[r][c] == 2:
            chicken_position.append((r, c))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 987654321
for positions in combinations(chicken_position, M):
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    for position in positions:
        visited[position[0]][position[1]] = 1
        queue.append((position[0], position[1], 0))
    home_cnt = 0
    total_distance = 0
    while queue:
        r, c, d = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, d + 1))
                if arr[nr][nc] == 1:
                    home_cnt += 1
                    total_distance += d + 1
                    if home_cnt == total_home_cnt:
                        queue = []
                        break
    answer = min(answer, total_distance)

print(answer)
