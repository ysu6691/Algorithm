import copy

testcase = int(input())

for tc in range(1, testcase+1):

    N, K = map(int, input().split())

    arr = []
    max_num = -1 # 가장 높은 높이
    min_num = 21 # 가장 낮은 높이

    # 2차원 배열에 등산로 저장하면서,
    # 가장 높은 높이와 가장 낮은 높이 구하기
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

        if max(row) > max_num:
            max_num = max(row)
        if min(row) < min_num:
            min_num = min(row)

    # 시작점(가장 높은 높이)구하기
    start_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_num:
                start_list.append((i, j))

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 길이 저장할 셋 생성
    length_set = set()

    # 배열 전체를 돌면서, 0 ~ K만큼 깎기
    for i in range(N):
        for j in range(N):

            for k in range(K+1):
                tmp_arr = copy.deepcopy(arr) # 깊은 복사
                tmp_arr[i][j] -= k

                # 만약 깎다가 높이가 -1이 됐다면, 그만 깎기
                if tmp_arr[i][j] == -1:
                    break

                # 시작점을 스택에 넣고 DFS 수행
                for start in start_list:
                    stack = [[start, 1]] # 스택에는 좌표와 현재 길이 저장
                    visited = []

                    while stack:
                        current = stack.pop()

                        length_set.add(current[1]) # pop 할 때마다 길이 저장

                        if current not in visited:
                            visited.append(current)

                            for d in range(4):
                                ni = current[0][0] + di[d]
                                nj = current[0][1] + dj[d]
                                length = current[1]

                                if 0 <= ni < N and 0 <= nj < N and [(ni, nj), length + 1] not in visited:
                                    # 더 낮다면(이동할 수 있다면) 스택에 넣기
                                    if tmp_arr[ni][nj] < tmp_arr[current[0][0]][current[0][1]]:
                                        stack.append([(ni, nj), length + 1])

    # 가장 긴 길이 출력
    print(f'#{tc} {max(length_set)}')