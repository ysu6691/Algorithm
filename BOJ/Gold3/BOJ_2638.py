import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
time = 0

while True:
    time += 1
    stack = [(0, 0)]
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    cnt_arr = [[0] * M for _ in range(N)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 1:
                    cnt_arr[nr][nc] += 1
                else:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
    
    zero_cnt = 0
    for r in range(N):
        for c in range(M):
            if cnt_arr[r][c] > 1:
                arr[r][c] = 0
            if not arr[r][c]:
                zero_cnt += 1
    if zero_cnt == N * M:
        break

print(time)