from collections import defaultdict

# 상어 이동
def shark_move():
    # key: 좌표, value: [상어 번호, 상어 방향]
    new_sharks = defaultdict(list)

    # 모든 상어가 이동하기 전에 냄새를 먼저 남겨야 한다.
    for shark in sharks:
        r = sharks[shark][0]
        c = sharks[shark][1]
        smells[(r, c)] = [shark, K] 

    # 상어 이동
    for shark in sharks:
        r = sharks[shark][0]
        c = sharks[shark][1]
        current_direction = sharks[shark][2]
        # 현재 보고 있는 방향에서 우선순위 순서대로 보기
        for d in shark_directions[shark][current_direction-1]:
            nr = sharks[shark][0] + dr[d]
            nc = sharks[shark][1] + dc[d]
            # 배열을 벗어나지 않고 냄새가 있지 않은 곳부터 확인
            if 0 <= nr < N and 0 <= nc < N and not smells[(nr, nc)]:
                # 갈 수 있다면 상어가 있는지 확인하고 더 큰 상어만 남기기
                if not new_sharks[(nr, nc)]:
                    new_sharks[(nr, nc)] = [shark, d]
                else:
                    if shark < new_sharks[(nr, nc)][0]:
                        new_sharks[(nr, nc)] = [shark, d]
                break

        # 네 방향 모두 이동할 수 없었다면, 자신의 냄새가 있는 방향으로 이동
        else:
            for d in shark_directions[shark][current_direction - 1]:
                nr = sharks[shark][0] + dr[d]
                nc = sharks[shark][1] + dc[d]
                if 0 <= nr < N and 0 <= nc < N and smells[(nr, nc)][0] == shark:
                    if not new_sharks[(nr, nc)]:
                        new_sharks[(nr, nc)] = [shark, d]
                    else:
                        if shark < new_sharks[(nr, nc)][0]:
                            new_sharks[(nr, nc)] = [shark, d]
                    break

    # 다시 원래 자료구조 형태로 변환하기
    # key: 상어 번호, value: [r, c, 방향]
    changed_sharks = defaultdict(list)
    for position in new_sharks:
        shark = new_sharks[position][0]
        direction = new_sharks[position][1]
        changed_sharks[shark] = [position[0], position[1], direction]

    return changed_sharks


# 냄새 줄이기
def reduce_smell():
    # 새로운 defaultdict에 저장해서 반환
    new_smells = defaultdict(list)
    for position in smells:
        if smells[position]:
            smells[position][1] -= 1
            # 냄새 없어지면 버리고 남은 냄새만 담기
            if smells[position][1]:
                new_smells[position] = smells[position][:]

    return new_smells

###############################################################

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
current_directions = list(map(int, input().split()))
sharks = defaultdict(list)
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            sharks[arr[i][j]] = [i, j, current_directions[arr[i][j]-1]]

# sharks
# key: 상어 번호, value: [r, c, 방향]

# 우선순위를 알려주는 자료구조 생성
shark_directions = defaultdict(list)
for i in range(1, M+1):
    shark_directions[i] = [list(map(int, input().split())) for _ in range(4)]

# shark_directions
# key: 상어 번호, value: [[], [], [], []] (방향 순서대로 우선순위를 담고 있음)

smells = defaultdict(list)
# smells
# key: 좌표, value: [상어 번호, 남은 냄새]

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

answer = 0

while True:
    sharks = shark_move()
    smells = reduce_smell()
    answer += 1
    if answer > 1000:
        answer = -1
        break
    if len(sharks) == 1:
        break

print(answer)