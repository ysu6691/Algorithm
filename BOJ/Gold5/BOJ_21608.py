from collections import defaultdict

N = int(input())
student_dict = defaultdict(list) # 키 생성과 동시에 리스트에 append

for _ in range(N**2):
    info = list(map(int, input().split()))
    for _ in range(4):
        student_dict[info[0]].append(info.pop())

arr = [[0]*N for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for student in student_dict:

    # 주변에 좋아하는 친구가 몇 명 있는지 나타내는 2차원 배열
    tmp_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] in student_dict[student]: # 만약 좋아하는 친구가 있다면,
                for k in range(4): # 사방탐색
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                        tmp_arr[ni][nj] += 1 # 그 자리가 빈자리라면, 카운트

    # 1번 조건을 만족하는 자리 구하기
    # 가장 카운트가 많이 된 자리만 positions 배열에 등록
    positions = []
    max_cnt = -1
    for i in range(N):
        for j in range(N):
            if not arr[i][j] and tmp_arr[i][j] > max_cnt:
                max_cnt = tmp_arr[i][j]
                positions = [(i, j)]
            elif not arr[i][j] and tmp_arr[i][j] == max_cnt:
                positions.append((i, j))

    # 2번 조건을 만족하는 자리 구하기
    # 가장 주변에 빈자리가 많은 자리를 max_blank_positions에 등록
    max_cnt = -1
    max_blank_positions = [] # 주변에 빈자리가 가장 많은 자리 구하는 배열
    for position in positions: # 1번 조건을 만족한 자리만 보기
        cnt = 0
        for k in range(4):
            ni = position[0] + di[k]
            nj = position[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not arr[ni][nj]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_blank_positions = [(position[0], position[1])]
        elif cnt == max_cnt:
            max_blank_positions.append((position[0], position[1]))

    # 3번 조건 구하기
    # 1, 2번 조건을 만족하는 자리를 오름차순 정렬 (행 -> 열 순으로)
    max_blank_positions.sort(key=lambda x: (x[0], x[1]))
    # 첫 번째 자리가 1, 2, 3번 조건을 모두 만족하는 자리
    arr[max_blank_positions[0][0]][max_blank_positions[0][1]] = student

# 정답 구하기
answer = 0

for i in range(N):
    for j in range(N):
        current = arr[i][j]
        cnt = 0

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in student_dict[current]:
                    cnt += 1
        if cnt > 0:
            answer += 10 ** (cnt-1)

print(answer)

