# 중력 작용
def gravity():
    # 빈 2차원 리스트 밑에서부터 채우기
    tmp_arr = [[100]*N for _ in range(N)]
    for i in range(N):
        height = N-1
        for j in range(N-1, -1, -1):
            if 0 <= arr[j][i] < 100:
                tmp_arr[height][i] = arr[j][i]
                height -= 1
            elif arr[j][i] == -1:
                tmp_arr[j][i] = -1
                height = j - 1
    return tmp_arr

# 90도 회전
def rotate():
    tmp_arr = [[100]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp_arr[i][j] = arr[j][N-i-1]
    return tmp_arr

##################################################

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

answer = 0

while True:
    max_cnt = -1
    max_cnt_zero = -1
    max_position_list = []
    normal_block_visited = set() # 0과 -1을 제외한 나머지 숫자는 DFS 재수행 x

    for i in range(N):
        for j in range(N):
            # 현재 블록이 일반 블록이고 방문하지 않았다면, DFS 수행
            if 1 <= arr[i][j] < 100 and (i, j) not in normal_block_visited:
                visited = set()
                tmp_position_list = [] # 인접한 같은 숫자의 블록과 무지개 블록 담기
                cnt = 0 # 인접한 블록 개수 세기
                stack = [(i, j)]
                cnt_zero = 0 # 무지개 블록 개수 세기

                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        cnt += 1
                        tmp_position_list.append((current[0], current[1])) # 인접 블록 담기
                        if not arr[current[0]][current[1]]: # 만약 무지개 블록이면,
                            cnt_zero += 1 # 카운트
                        else: # 만약 일반 블록이면,
                            normal_block_visited.add((current[0], current[1])) # 방문했다고 체크 

                        for k in range(4):
                            ni = current[0] + di[k]
                            nj = current[1] + dj[k]
                            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and (ni, nj) not in normal_block_visited:
                                if arr[ni][nj] == arr[i][j] or not arr[ni][nj]: # 같은 블록이거나 무지개 블록인 경우
                                    stack.append((ni, nj))

                # 찾은 블록 수가 2보다 작거나 가장 큰 블록 그룹이 아닌 경우, continue
                if cnt < max_cnt or cnt < 2:
                    continue
                # 만약 가장 큰 블록 그룹과 크기가 같다면,
                elif cnt == max_cnt:
                    if cnt_zero < max_cnt_zero: # 무지개 블록 개수 비교 (더 적으면 continue)
                        continue
                    elif cnt_zero == max_cnt_zero: # 무지개 블록 개수도 같다면,
                        # 기준 블록 행, 열 비교
                        if i < max_position[0]:
                            continue
                        elif i == max_position[0]:
                            if j <= max_position[1]:
                                continue

                # continue 되지 않은 블록이 가장 큰 블록임
                max_cnt = cnt # 최댓갑 갱신
                max_position_list = tmp_position_list[:] # 블록들 위치 기억
                max_cnt_zero = cnt_zero # 그떄의 무지개 블록 수 기억
                max_position = (i, j) # 그때의 기준 블록 위치 기억

    # 만약 가장 큰 블록을 못 찾았다면, 종료
    if max_cnt == -1:
        break

    # 값 누적
    answer += max_cnt ** 2
    # 빈 칸은 100으로 표시
    for position in max_position_list:
        arr[position[0]][position[1]] = 100

    # 중력 -> 90도 회전 -> 중력
    arr = gravity()
    arr = rotate()
    arr = gravity()

print(answer)
