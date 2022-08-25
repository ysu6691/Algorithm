testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    find_start = False

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j, 0) # 행, 열, 거리를 저장
                find_start = True
                break
        if find_start:
            break

    queue = [start]
    visited = set()
    finish = False
    result = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        # 행, 열, 거리를 각 변수에 저장
        (y, x, cnt) = queue.pop(0)
        if (y, x) not in visited:
            visited.add((y, x))

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    if arr[ny][nx] != 1:
                        # 현재 거리에 1을 추가해 queue에 저장
                        queue.append((ny, nx, cnt+1))
                    if arr[ny][nx] == 3:
                        result = cnt
                        finish = True
                        break

        if finish:
            break

    print(f'#{tc} {result}')