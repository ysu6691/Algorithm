# 0으로 바꾸는 마법
def magic():
    r = N // 2
    c = N // 2
    for i in range(1, s+1):
        arr[r + dr[d-1]*i][c + dc[d-1]*i] = 0


# 빈 칸 생겼을 때 구슬 이동
# 중앙에서부터 밖으로 나가면서 queue에 넣기
def move():
    r = N // 2
    c = N // 2
    direction = 2 # 처음 시작은 왼쪽으로
    queue = []
    # 밖으로 돌면서 확인
    for cnt in cnt_list:
        # cnt만큼 이동
        for _ in range(cnt):
            r += dr[direction]
            c += dc[direction]
            # 만약 구슬이 있다면, queue에 넣기
            if arr[r][c]:
                queue.append(arr[r][c])
        # 방향 변경
        direction = change_direction[direction]

    # 빈 2차원 배열을 똑같이 돌면서 queue에서 뺀 값 넣기
    r = N // 2
    c = N // 2
    tmp_arr = [[0] * N for _ in range(N)]
    direction = 2
    finish = False
    for cnt in cnt_list:
        for _ in range(cnt):
            r += dr[direction]
            c += dc[direction]
            if queue:
                tmp_arr[r][c] = queue.pop(0)
            else:
                finish = True
                break
        direction = change_direction[direction]
        if finish:
            break

    return tmp_arr # 이동한 배열 반환


# 폭발
# 중앙에서 밖으로 나가면서, 4개 이상인 구슬 폭발
def explosion():
    global answer
    r = N // 2
    c = N // 2
    direction = 2
    current = 0
    explosion_list = []
    flag = False
    finish = False

    for cnt in cnt_list:
        for _ in range(cnt):
            r += dr[direction]
            c += dc[direction]
            # 현재 구슬이 current와 같다면, 리스트에 추가
            if arr[r][c] == current:
                explosion_list.append((r, c))
            # 현재 구슬이 전 구슬과 다르다면,
            else:
                # 길이가 4 이상인지 확인
                if len(explosion_list) >= 4:
                    flag = True
                    # 결과 누적하면서 0으로 만들기
                    for position in explosion_list:
                        answer += arr[position[0]][position[1]]
                        arr[position[0]][position[1]] = 0
                # current 값 변경
                current = arr[r][c]
                explosion_list = [(r, c)]
        # 방향 변경
        direction = change_direction[direction]
        if finish:
            break

    # 만약 폭발한 구슬이 있다면, True 반환
    if flag:
        return True
    return False


# 구슬을 그룹으로 만들어서 바꾸기
def change_bead():
    r = N // 2
    c = N // 2
    direction = 2
    current = 0
    merge = 0
    queue = []

    # 중앙에서 밖으로 나가면서 확인
    # 구슬의 수와 구슬 번호를 차례대로 queue에 추가 
    for cnt in cnt_list:
        for _ in range(cnt):
            r += dr[direction]
            c += dc[direction]
            if arr[r][c] == current:
                merge += 1
            else:
                # current가 0이 아닐 때만 queue에 추가
                if current:
                    queue.append(merge)
                    queue.append(current)
                current = arr[r][c]
                merge = 1
        direction = change_direction[direction]

    # move 함수와 동일하게, 빈 2차원 리스트에 queue에서 뺀 값 넣기
    r = N // 2
    c = N // 2
    tmp_arr = [[0] * N for _ in range(N)]
    direction = 2
    finish = False
    for cnt in cnt_list:
        for _ in range(cnt):
            r += dr[direction]
            c += dc[direction]
            if queue:
                tmp_arr[r][c] = queue.pop(0)
            else:
                finish = True
                break
        direction = change_direction[direction]
        if finish:
            break

    return tmp_arr


###############################################################


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 방향 변경 (왼쪽 -> 밑, 밑 -> 오른쪽, 오른쪽 -> 위, 위 -> 왼쪽)
change_direction = {0: 2, 1: 3, 2: 1, 3: 0}

# 얼만큼 가야 방향을 변경할지 알려주는 리스트
cnt_list = []
for i in range(1, N):
    cnt_list.append(i)
    cnt_list.append(i)
cnt_list.append(N - 1)
# ex) N = 3
# cnt_list = [1, 1, 2, 2, 2]

answer = 0

# 시작
for i in range(M):
    d, s = map(int, input().split())
    magic()
    arr = move()
    while explosion():
        arr = move()
    arr = change_bead()

print(answer)
