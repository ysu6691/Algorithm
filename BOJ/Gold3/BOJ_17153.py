import copy

# 궁수 자리 잡는 조합 함수
def comb(sidx, idx):
    if sidx == 3:
        position_list.append(selection[:])
        return

    if idx == M:
        return

    selection[sidx] = positions[idx]
    comb(sidx+1, idx+1)
    comb(sidx, idx+1)


# 변수 저장
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 궁수가 자리잡을 수 있는 모든 경우의 수 구하기
positions = [i for i in range(M)]
check = [0]*M
selection = [0]*3
position_list = []
comb(0, 0)


# 궁수 공격 범위 구하기 (왼쪽에서부터 공격)
ax = []
ay = []

for i in range(1, D+1):
    dx = [0]
    for j in range(1, i):
        dx.insert(0, -j)
        dx.append(j)
    ax += dx

    dy = [-i]
    for j in range(1, i):
        dy.insert(0, -(i-j))
        dy.append(-(i-j))
    ay += dy

# ex) D = 2
#     ax = [0, -1, 0, 1]
#     ay = [-1, -1, -2, -1]


max_cnt = 0


# 궁수 위치 정하기
for position in position_list:
    # 궁수 위치 변할때마다 격자판과 카운트 리셋
    tmp_arr = copy.deepcopy(arr)
    cnt = 0

    # 라운드가 진행될 때마다 궁수 위로 한 칸 이동
    for y in range(N, 0, -1):
        # 적을 잡았다면, 그 자리를 기억해뒀다가 중복으로 카운트 되지 않도록 처리
        attacked_position = []

        # 각 궁수 지정
        for x in position:

            # 거리를 늘려가면서 적이 있나 확인
            for i in range(D**2):
                attack_x = x + ax[i]
                attack_y = y + ay[i]

                if 0 <= attack_x < M and 0 <= attack_y < N:
                    # 적이 있을 때 이미 잡았던 적이라면 다음 궁수로 넘어가기
                    # 처음 잡는 적이라면 cnt + 1 / 잡은 적 기억하고 다음 궁수로 넘어가기
                    if tmp_arr[attack_y][attack_x] == 1:
                        if [attack_y, attack_x] in attacked_position:
                            break
                        cnt += 1
                        attacked_position.append([attack_y, attack_x])
                        break

        # 모든 궁수가 공격을 끝내면, 잡았던 자리 0으로 표시
        for j in attacked_position:
            tmp_arr[j[0]][j[1]] = 0

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)


