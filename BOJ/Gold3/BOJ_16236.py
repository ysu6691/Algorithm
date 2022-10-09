from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = (i, j)
            queue.append((i, j))
            arr[i][j] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

size = 2
eat_cnt = 0
time = 0

while True:
    visited = set()
    candidate = []
    tmp_time = -1
    if eat_cnt == size:
        size += 1
        eat_cnt = 0

    while queue:
        tmp_time += 1

        for _ in range(len(queue)):
            current = queue.popleft()

            if current not in visited:
                visited.add(current)
                if arr[current[0]][current[1]] != 0 and arr[current[0]][current[1]] < size:
                    candidate.append((current[0], current[1]))

                for i in range(4):
                    nr = current[0] + dr[i]
                    nc = current[1] + dc[i]

                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                        if arr[nr][nc] <= size:
                            queue.append((nr, nc))

        if candidate:
            candidate.sort(key=lambda x: (x[0], x[1]))
            next_position = candidate[0]
            arr[next_position[0]][next_position[1]] = 0
            queue = deque([next_position])
            eat_cnt += 1
            time += tmp_time
            start = next_position
            break

    if not queue:
        break

print(time)
