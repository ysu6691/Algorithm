for tc in range(1, 11):

    N, start = map(int, input().split())
    N_list = list(map(int, input().split()))
    max_num = max(N_list) # 인접 행렬의 크기를 정하기 위해, 가장 큰 번호 받아오기

    # 가장 큰 번호만큼의 인접 행렬 생성
    adj_matrix = [[0]*(max_num+1) for _ in range(max_num+1)]

    # 갈 수 있는 곳 체크
    for i in range(N//2):
        s = N_list[i*2]
        e = N_list[i*2 + 1]
        adj_matrix[s][e] = 1

    queue = [[start, 0]]
    visited = []

    max_length = -1
    max_list = []

    # BFS 실시
    while queue:
        # current = [현재 번호, 지금까지 거리]
        current = queue.pop(0)

        # 만약 거리가 현재 최대 거리보다 길다면, 최대 거리 및 리스트 초기화
        if current[1] > max_length:
            max_length = current[1]
            max_list = [current[0]]
        # 만약 거리가 현재 최대 거리와 같다면, 리스트에 추가
        elif current[1] == max_length:
            max_list.append(current[0])

        if current[0] not in visited:
            visited.append(current[0])

            for destination in range(max_num+1):
                if adj_matrix[current[0]][destination] and destination not in visited:
                    queue.append([destination, current[1]+1]) # queue에 현재 거리 + 1 정보를 포함해 추가

    # 시작점에서부터 거리가 가장 긴 번호 중 최댓값 출력
    print(f'#{tc} {max(max_list)}')