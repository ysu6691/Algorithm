# [0, 0]에서부터 DFS를 수행하다가 치즈를 만나면 해당 위치를 기억
# 끝까지 탐색이 끝나면, 기억한 위치를 모두 0으로 바꾸기

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

time = 0

# 처음 치즈 개수 입력
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            result += 1

# 시간이 지날때마다 [0,0]에서부터 DFS 재실시
while True:
    stack = [(0, 0)]
    visited = set()
    positions = set() # 겉에 있는 치즈 위치를 기억할 셋 생성
    time += 1 # 시간
    cnt = 0 # 한시간이 지난 후 치즈 개수를 입력

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            for i in range(4):
                nr = current[0] + dr[i]
                nc = current[1] + dc[i]

                if 0 <= nr < N and 0 <= nc < M:
                    # 치즈가 있다면, 위치를 기억 (stack에는 추가 x)
                    if arr[nr][nc] == 1:
                        positions.add((nr, nc))
                    elif arr[nr][nc] == 0:
                        if (nr, nc) not in visited:
                            stack.append((nr, nc))

    # DFS가 끝나면 기억해두었던 위치를 0으로 표시
    for position in positions:
        arr[position[0]][position[1]] = 0

    # 현재 치즈 개수 세기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1

    # 치즈가 없다면, while문 종료
    if not cnt:
        break

    # 치즈가 있다면, 현재 치즈 개수 갱신
    result = cnt

print(time, result)
