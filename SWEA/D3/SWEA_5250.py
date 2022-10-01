testcase = int(input())
for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 987654321
    visited = set()
    distance = [[INF]*N for _ in range(N)]
    candidates = {(0, 0)}

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    distance[0][0] = 0

    while candidates:

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
                if (ni, nj) not in visited:
                    tmp = max(0, arr[ni][nj] - arr[current[0]][current[1]]) + distance[current[0]][current[1]] + 1
                    if tmp < distance[ni][nj]:
                        distance[ni][nj] = tmp
                        candidates.add((ni, nj))

    print(f'#{tc} {distance[-1][-1]}')