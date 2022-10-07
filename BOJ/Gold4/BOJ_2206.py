from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque([(0, 0, 0)])
answer = -1

while queue:
    current = queue.popleft()
    r, c, broke = current[0], current[1], current[2]
    if r == N-1 and c == M-1:
        answer = visited[r][c][broke]
        break

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] and not broke:
                queue.append((nr, nc, 1))
                visited[nr][nc][1] = visited[r][c][0] + 1
            elif not arr[nr][nc] and not visited[nr][nc][broke]:
                queue.append((nr, nc, broke))
                visited[nr][nc][broke] = visited[r][c][broke] + 1

print(answer)