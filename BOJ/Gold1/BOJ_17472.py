N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            arr[i][j] = 100

num = 1
visited = []

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 100:
            stack = [(i, j)]

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.append(current)
                    arr[current[0]][current[1]] = num

                    for k in range(4):
                        ni = current[0] + di[k]
                        nj = current[1] + dj[k]

                        if 0 <= ni < N and 0 <= nj < M:
                            if arr[ni][nj] and (ni, nj) not in visited:
                                stack.append((ni, nj))

            num += 1

INF = 999
adj_matrix = [[INF]*num for i in range(num)]
distance = [INF]*num
visited = [0]*num

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            current = arr[i][j]

            for k in range(1, i+1):
                if arr[i-k][j] == arr[i][j]:
                    break
                elif arr[i-k][j]:
                    if k - 1 < 2:
                        break
                    adj_island = arr[i-k][j]
                    if k - 1 < adj_matrix[current][adj_island]:
                        adj_matrix[current][adj_island] = k - 1
                        adj_matrix[adj_island][current] = k - 1
                        break
                    else:
                        break

            for k in range(1, N-i):
                if arr[i+k][j] == arr[i][j]:
                    break
                elif arr[i+k][j]:
                    if k - 1 < 2:
                        break
                    adj_island = arr[i+k][j]
                    if k - 1 < adj_matrix[current][adj_island]:
                        adj_matrix[current][adj_island] = k - 1
                        adj_matrix[adj_island][current] = k - 1
                        break
                    else:
                        break

            for k in range(1, j+1):
                if arr[i][j-k] == arr[i][j]:
                    break
                elif arr[i][j-k]:
                    if k - 1 < 2:
                        break
                    adj_island = arr[i][j-k]
                    if k - 1 < adj_matrix[current][adj_island]:
                        adj_matrix[current][adj_island] = k - 1
                        adj_matrix[adj_island][current] = k - 1
                        break
                    else:
                        break

            for k in range(1, M-j):
                if arr[i][j+k] == arr[i][j]:
                    break
                elif arr[i][j+k]:
                    if k - 1 < 2:
                        break
                    adj_island = arr[i][j+k]
                    if k - 1 < adj_matrix[current][adj_island]:
                        adj_matrix[current][adj_island] = k - 1
                        adj_matrix[adj_island][current] = k - 1
                        break
                    else:
                        break

distance[1] = 0
for i in range(1, num):

    min_distance = INF
    for j in range(1, num):
        if not visited[j] and distance[j] < min_distance:
            current = j
            min_distance = distance[j]
    visited[current] = 1

    for j in range(1, num):
        if not visited[j] and adj_matrix[current][j] < distance[j]:
            distance[j] = adj_matrix[current][j]

answer = sum(distance[1:])
if sum(distance[1:]) >= 999:
    answer = -1
print(answer)