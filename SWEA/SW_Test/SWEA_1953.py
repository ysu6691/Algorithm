testcase = int(input())

for tc in range(1, testcase+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 리스트의 인덱스는 구조물의 번호
    # 구조물마다 이동할 수 있는 위치 저장
    di = [[], [-1, 1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
    dj = [[], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]

    # 큐에는 현재 위치와 이동 거리 저장
    queue = [[R, C, 1]]
    visited = []
    cnt = 0 # 이동할 수 있는 장소 개수 저장할 변수

    while queue:
        current = queue.pop(0)
        if current[2] > L: # 만약 이동할 수 있는 시간을 넘었다면, continue
            continue

				# 아직 방문하지 않았다면, 방문 후 cnt + 1
        if [current[0], current[1]] not in visited: 
            visited.append([current[0], current[1]])
            cnt += 1

            move = arr[current[0]][current[1]] # 터널 구조물을 확인한 후,
            for k in range(len(di[move])):     # 이동
                ni = current[0] + di[move][k]
                nj = current[1] + dj[move][k]

								# 다음 위치에 아직 방문하지 않았고 터널이 있다면,
                if 0 <= ni < N and 0 <= nj < M:
                    if [ni, nj] not in visited and arr[ni][nj]: 
												# 이동할 수 있는지 확인
                        if current[0] < ni:
                            if arr[ni][nj] == 3 or arr[ni][nj] == 5 or arr[ni][nj] == 6:
                                continue
                        elif current[0] > ni:
                            if arr[ni][nj] == 3 or arr[ni][nj] == 4 or arr[ni][nj] == 7:
                                continue
                        elif current[1] < nj:
                            if arr[ni][nj] == 2 or arr[ni][nj] == 4 or arr[ni][nj] == 5:
                                continue
                        elif current[1] > nj:
                            if arr[ni][nj] == 2 or arr[ni][nj] == 6 or arr[ni][nj] == 7:
                                continue
                        queue.append([ni, nj, current[2]+1])

    print(f'#{tc} {cnt}')