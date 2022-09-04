# 2차원 배열을 돌면서, 울타리가 아닌 곳을 찾으면 DFS 수행
# 양과 늑대 개수를 알아내서 더 큰 쪽에 더해주기

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

alive_sheep = 0
alive_wolf = 0

visited = set()

# 2차원 배열을 돌면서 DFS 수행
for i in range(R):
    for j in range(C):
        stack = [(i, j)]
        sheep = 0
        wolf = 0

        # 이미 방문했거나 울타리라면, 넘어가기
        if stack[0] in visited or arr[i][j] == '#':
            continue

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)

                if arr[current[0]][current[1]] == 'o':
                    sheep += 1
                elif arr[current[0]][current[1]] == 'v':
                    wolf += 1

                for k in range(4):
                    nr = current[0] + dr[k]
                    nc = current[1] + dc[k]

                    if 0 <= nr < R and 0 <= nc < C:
                        destination = arr[nr][nc]

                        if destination != '#':
                            if (nr, nc) not in visited:
                                stack.append((nr, nc))

        if sheep > wolf:
            alive_sheep += sheep
        else:
            alive_wolf += wolf

print(alive_sheep, alive_wolf)