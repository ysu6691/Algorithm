testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    find_finish = False

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
                find_finish = True
                break

        if find_finish == True:
            break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [start]
    visited = []
    result = 0
    finish = False

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)

            for i in range(4):
                nx = current[1] + dx[i]
                ny = current[0] + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if [ny, nx] not in visited and maze[ny][nx] == 0:
                        stack.append([ny, nx])

                    if maze[ny][nx] == 3:
                        result = 1
                        finish = True
                        break

        if finish:
            break

    print(f'#{tc} {result}')
