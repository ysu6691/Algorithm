testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    find_finish = False

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = [i, j]
                find_finish = True
                break

        if find_finish == True:
            break

    stack = [start]
    visited_matrix = [[0]*N for i in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    finish = False

    result = 0

    while stack:
        current = stack.pop()
        if not visited_matrix[current[0]][current[1]]:
            visited_matrix[current[0]][current[1]] = 1

            for i in range(4):
                nx = current[1] + dx[i]
                ny = current[0] + dy[i]

                if 0 <= nx < N and 0 <= ny < N and not visited_matrix[ny][nx]:
                    if arr[ny][nx] == 3:
                        result = 1
                        finish = True
                        break

                    elif arr[ny][nx] == 0:
                        stack.append([ny, nx])

    print(f'#{tc} {result}')