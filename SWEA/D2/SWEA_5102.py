testcase = int(input())

for tc in range(1, testcase+1):

    V, E = map(int, input().split())
    adj_matrix = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        adj_matrix[start][end] = 1
        adj_matrix[end][start] = 1

    start, end = map(int, input().split())

    # queue에 시작점과 초기값(0)을 저장
    queue = [[start, 0]]
    visited = []
    result = 0
    finish = False

    while queue:
        # queue에 현재 좌표와 시작점으로부터의 거리를 저장
        [current, cnt] = queue.pop(0)

        if current not in visited:
            visited.append(current)

            for destination in range(V+1):
                if adj_matrix[current][destination] and destination not in visited:
                    # queue에 다음 좌표와 현재 거리 + 1을 저장
                    queue.append([destination, cnt + 1])

                    if destination == end:
                        result = cnt + 1
                        finish = True
                        break

        if finish:
            break

    print(f'#{tc} {result}')