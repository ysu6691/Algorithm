def escape(location):
    global result
    if maze[location[0]][location[1]] == 2:
        result = 1
        return

    for i in range(4):
        nx = location[1] + dx[i]
        ny = location[0] + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if [ny, nx] not in visited and maze[ny][nx] != 1:
                visited.append([ny, nx])
                escape([ny, nx])

testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    find_start = False

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                start = [i, j]
                find_start = True
                break

        if find_start == True:
            break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = []
    result = 0

    escape(start)

    print(f'{tc} {result}')
