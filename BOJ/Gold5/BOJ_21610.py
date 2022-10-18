# 구름 이동하는 함수
def move(direction, distance):
    for cloud in clouds:
        # 한번에 이동해서 시간 줄이기
        cloud[0] += dr[direction] * distance
        cloud[1] += dc[direction] * distance
        cloud[0] %= N
        cloud[1] %= N
        # 이후 시간단축을 위해 셋에 현재 구름 위치 담기
        set_clouds.add(tuple(cloud))

# 비 내리는 함수
def rain():
    # 일단 구름 있는 곳은 1씩 추가
    for cloud in clouds:
        arr[cloud[0]][cloud[1]] += 1

    # 주변 대각선 위치에 저장된 물이 있다면, 그만큼 또 추가
    for cloud in clouds:
        cnt = 0
        for i in [2, 4, 6, 8]:
            nr = cloud[0] + dr[i]
            nc = cloud[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                cnt += 1
        arr[cloud[0]][cloud[1]] += cnt

# 새로운 구름 만드는 함수
def make_clouds():
    new_clouds = []
    for i in range(N):
        for j in range(N):
            # 2보다 크고 원래 구름이 아니라면, 2 감소시키고 새 구름에 추가
            # 아까 만든 셋을 이용해 시간 단축
            if arr[i][j] >= 2 and (i, j) not in set_clouds:
                arr[i][j] -= 2
                new_clouds.append([i, j])
    return new_clouds

#################################################################

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for _ in range(M):
    d, s = map(int, input().split())
    set_clouds = set()
    move(d, s) # 이동
    rain() # 비내리기
    clouds = make_clouds() # 새로운 구름 만들기

# 정답 출력
answer = 0
for i in range(N):
    for j in range(N):
        answer += arr[i][j]
print(answer)
