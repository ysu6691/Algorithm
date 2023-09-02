import sys
from itertools import combinations
input = sys.stdin.readline

arr = [input() for _ in range(5)]
total_positions = []
for i in range(5):
    for j in range(5):
        total_positions.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 0
for positions in combinations(total_positions, 7):
    stack = [positions[0]]
    visited = {positions[0]}
    S_cnt = 0
    cnt = 0
    while stack:
        current = stack.pop()
        if current in positions:
            cnt += 1
        if arr[current[0]][current[1]] == "S":
            S_cnt += 1
        for i in range(4):
            nr = current[0] + dr[i]
            nc = current[1] + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in visited and (nr, nc) in positions:
                stack.append((nr, nc))
                visited.add((nr, nc))
    if S_cnt >= 4 and cnt == 7:
        answer += 1

print(answer)
