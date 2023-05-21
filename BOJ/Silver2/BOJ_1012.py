import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):

    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = set()
    answer = 0
    for r in range(N):
        for c in range(M):
            if (r, c) in visited or not arr[r][c]:
                continue
            
            stack = [(r, c)]
            answer += 1
            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                visited.add(current)

                for d in range(4):
                    nr = current[0] + dr[d]
                    nc = current[1] + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and arr[nr][nc]:
                        stack.append((nr, nc))
    print(answer)