
# 벽을 놓을 수 있는 모든 경우를 다 고려해서, DFS 수행

import copy

# 벽을 놓을 수 있는 모든 경우 구하기
def set_walls(sidx, idx):
    if sidx == 3:
        wall_positions.append(selection[:])
        return
    if idx == len(positions):
        return
    selection[sidx] = positions[idx]
    set_walls(sidx+1, idx+1)
    set_walls(sidx, idx+1)

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 0인 경우에만 벽 놓기
positions = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            positions.append((i, j))

selection = [0]*3
wall_positions = []
set_walls(0, 0)

# wall_positions = [[(0, 1), (0, 2), (0, 3)], [(0, 1), (0, 2), (0, 6)], ...]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

max_area = -1

# 벽 세 개 고르기
for walls in wall_positions:
    area = 0
    tmp_area = copy.deepcopy(arr) # 원래 배열은 그대로 두고 깊은 복사

    # 벽 세우기
    for wall in walls:
        tmp_area[wall[0]][wall[1]] = 1
        visited = set() # visited를 셋으로 해서 시간 단축

    # 2차원 배열을 돌면서 2를 발견하면, DFS 수행
    for i in range(N):
        for j in range(M):
            if tmp_area[i][j] == 2:
                if (i, j) in visited: # 이미 봤던 곳이면 건너뛰도록 함으로써 시간 단축
                    continue
                    
                stack = [(i, j)]

                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        tmp_area[current[0]][current[1]] = 2

                        for k in range(4):
                            ni = current[0] + di[k]
                            nj = current[1] + dj[k]

                            if 0 <= ni < N and 0 <= nj < M:
                                if tmp_area[ni][nj] == 0:
                                    if (ni, nj) not in visited:
                                        stack.append((ni, nj))

    # 0인 영역 구하기
    for i in range(N):
        for j in range(M):
            if tmp_area[i][j] == 0:
                area += 1

    if area > max_area:
        max_area = area

print(max_area)

