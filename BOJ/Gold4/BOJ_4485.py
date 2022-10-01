problem = 0
while True:
    problem += 1
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 987654321
    visited = set()
    distance = [[INF]*N for _ in range(N)]
    candidates = [(0, 0)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    distance[0][0] = arr[0][0]

    while True:

        min_distance = INF
        for candidate in candidates:
            i = candidate[0]
            j = candidate[1]
            if (i, j) not in visited and distance[i][j] < min_distance:
                min_distance = distance[i][j]
                current = (i, j)
        visited.add(current)
        candidates.remove((current[0], current[1]))

        for k in range(4):
            ni = current[0] + di[k]
            nj = current[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if (ni, nj) not in visited and arr[ni][nj] + distance[current[0]][current[1]] < distance[ni][nj]:
                    distance[ni][nj] = arr[ni][nj] + distance[current[0]][current[1]]
                    candidates.append((ni, nj))

        if distance[-1][-1] != INF:
            break

    print(f'Problem {problem}: {distance[-1][-1]}')