from collections import defaultdict

testcase = int(input())

for tc in range(1, testcase+1):
    N, M, K = map(int, input().split())
    cells = defaultdict(list)

    # key는 좌표, value는 [남은 비활성 상태, 남은 활성 상태, 원래 생명력 수치]
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(M):
            if line[j]:
                cells[(i, j)] = [line[j], line[j], line[j]]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for _ in range(K):
        # 새로 생긴 세포의 정보를 담을 defaultdict 생성
        new_cells = defaultdict(list)
        for position, status in cells.items():

            # 만약 아직 비활성 상태라면, 비활성 상태 1 감소
            if status[0]:
                status[0] -= 1


            # 만약 활성 상태라면,
            elif status[1]:
                status[1] -= 1 # 일단 활성 상태 1 감소
                for i in range(4):
                    nr = position[0] + dr[i]
                    nc = position[1] + dc[i]

                    # 사방탐색 후 기존에 없던 자리면, new_cells에 추가
                    # (key는 좌표, value는 생명력 수치)
                    if (nr, nc) not in cells:
                        new_cells[(nr, nc)].append(status[2])

        # 새로 생긴 세포들만 보기
        for position in new_cells:
            # 만약 그 자리에 한 세포만 생겼다면, 그대로 기존 세포에 추가
            if len(new_cells[position]) == 1:
                cells[position] = [new_cells[position][0], new_cells[position][0], new_cells[position][0]]
            # 만약 그 자리에 여러 세포가 생길 수 있다면, 가장 생명력 수치가 큰 세포를 추가
            else:
                new_cells[position].sort()
                cells[position] = [new_cells[position][-1], new_cells[position][-1], new_cells[position][-1]]

    # 아직 살아있는 세포 세기
    answer = 0
    for cell in cells.values():
        # 비활성상태거나 활성상태인 경우만 세기
        if cell[0] or cell[1]:
            answer += 1

    print(f'#{tc} {answer}')
