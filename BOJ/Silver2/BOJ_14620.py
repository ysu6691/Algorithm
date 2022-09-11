# 조합으로 꽃 위치 세 개 선정
# 모든 조합을 확인해, 가격이 적은 조합을 찾기

# 씨앗 위치 선정
def set_position(sidx, idx):
    if sidx == 3:
        comb_positions.append(selection[:])
        return

    # N이 6이라면 놓을 수 있는 위치는 4 * 4
    # position_list = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), ... , (4, 4)]
    if idx == (N - 2) ** 2:
        return

    selection[sidx] = position_list[idx]
    set_position(sidx+1, idx+1)
    set_position(sidx, idx+1)


N = int(input())

cost_arr = [list(map(int, input().split())) for _ in range(N)]

# 놓을 수 있는 씨앗 위치 선정
position_list = []
for i in range(1, N-1):
    for j in range(1, N-1):
        position_list.append((i, j))

comb_positions = []
selection = [0]*3
set_position(0, 0)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 가격
min_cost = 200 * 5 * 3 + 1

# comb_positions = [[(1, 1), (1, 2), (1, 3)], ...]
# positions = [(1, 1), (1, 2), (1, 3)]
for positions in comb_positions:

    flower_arr = [[0] * N for _ in range(N)] # 화단 생성
    cost = 0
    flag = False

    for position in positions:
        x = position[1]
        y = position[0]

        # 이미 꽃이 있으면 break
        if flower_arr[y][x] == 1:
            break
            
        flower_arr[y][x] = 1    # 씨앗 위치 표시
        cost += cost_arr[y][x]  # 가격 갱신

        # 꽃 피었을 때도 똑같이
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if flower_arr[ny][nx] == 1:
                flag = True
                break

            flower_arr[ny][nx] = 1
            cost += cost_arr[ny][nx]

        if flag:
            break

    else:
        if cost < min_cost:
            min_cost = cost

print(min_cost)