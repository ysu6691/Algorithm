testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    find_start = False

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)
                find_start = True
                break
        if find_start:
            break

    queue = [start]
    visited = set()
    finish = False
    result = 0

    # 시작점으로부터 거리를 저장할 매트릭스 생성
    cnt_matrix = [[0]*N for _ in range(N)]
    cnt_matrix[start[0]][start[1]] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        (y, x) = queue.pop(0)
        if (y, x) not in visited:
            visited.add((y, x))

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and (ny, nx) not in visited:
                    if arr[ny][nx] != 1:
                        queue.append((ny, nx))
                        # 거리를 저장한 매트릭스에 현재 거리 + 1을 저장
                        cnt_matrix[ny][nx] = cnt_matrix[y][x] + 1
                    if arr[ny][nx] == 3:
                        result = cnt_matrix[y][x]
                        finish = True
                        break

        if finish:
            break

    print(f'#{tc} {result}')