testcase = int(input())

for tc in range(1, testcase + 1):
    N, M, K = map(int, input().split())
    colony_info = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0] * N for _ in range(N)]

    # 미생물 현재 위치에 정보(미생물 수, 이동 방향) 입력
    for colony in colony_info:
        arr[colony[0]][colony[1]] = [colony[2], colony[3]]
    '''
    ex)
    arr = [[0, 0, 0, 0, 0, 0, 0], 
           [0, [7, 1], 0, 0, 0, [8, 2], 0], 
           [0, [7, 1], 0, 0, 0, 0, 0], 
           [0, 0, [8, 4], 0, [3, 3], [100, 1], 0], 
           [0, 0, 0, [14, 1], 0, 0, 0], 
           [0, [5, 4], 0, 0, 0, [1, 1], 0], 
           [0, 0, 0, 0, 0, 0, 0]]
    '''

    move_dict = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    change_direction = {1: 2, 2: 1, 3: 4, 4: 3}

    # 시간 흐를 때마다 미생물 이동시키기
    for _ in range(M):
        info_dict = dict()
        for i in range(N):
            for j in range(N):
                if arr[i][j]:  # 만약 현재 위치에 미생물이 있다면,
                    current = arr[i][j]
                    arr[i][j] = 0  # 일단 현재 위치 비우기
                    ni = i + move_dict[current[1]][0]  # 이동
                    nj = j + move_dict[current[1]][1]  # 이동

                    # 만약 벽에 닿았다면,
                    if ni == 0 or ni == N - 1 or nj == 0 or nj == N - 1:
                        current[0] //= 2  # 반으로 줄이기
                        current[1] = change_direction[current[1]]  # 이동방향 바꾸기

                        # 만약 이동한 위치에 혼자 있다면,
                    if (ni, nj) not in info_dict:
                        info_dict[(ni, nj)] = [(current[0], current[1])]  # 딕셔너리 키 생성
                    else:  # 만약 다른 미생물이 있다면,
                        info_dict[(ni, nj)].append((current[0], current[1]))  # 딕셔너리에 추가

        '''
        ex) key는 좌표, value는 해당 좌표에 위치하는 미생물 정보
        info_dict = {(0, 1): [(3, 2)], (2, 5): [(8, 2), (100, 1)], 
                     (1, 1): [(7, 1)], (3, 3): [(8, 4), (3, 3), (14, 1)], 
                     (5, 2): [(5, 4)], (4, 5): [(1, 1)]}
        '''

        for position, info in info_dict.items():
            if len(info) == 1:  # 만약 혼자라면,
                arr[position[0]][position[1]] = list(info[0])  # 행렬에 정보 저장
            else:  # 여럿이라면,
                acc = 0
                max_num = -1
                for k in range(len(info)):
                    acc += info[k][0]  # 미생물 합치기
                    if info[k][0] > max_num:
                        max_num = info[k][0]  # 가장 큰 값을 가진 미생물의
                        direction = info[k][1]  # 방향 저장
                arr[position[0]][position[1]] = [acc, direction]  # 행렬에 정보 저장

    result = 0

    # 시간이 다 지난 후, 남아있는 미생물 수 출력
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                result += arr[i][j][0]

    print(f'#{tc} {result}')