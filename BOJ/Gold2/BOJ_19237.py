from collections import defaultdict

def shark_move():
    new_sharks = defaultdict(list)

    for shark in sharks:
        r = sharks[shark][0]
        c = sharks[shark][1]
        smells[(r, c)] = [shark, K]

    for shark in sharks:
        r = sharks[shark][0]
        c = sharks[shark][1]
        current_direction = sharks[shark][2]
        for d in shark_directions[shark][current_direction-1]:
            nr = sharks[shark][0] + dr[d]
            nc = sharks[shark][1] + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not smells[(nr, nc)]:
                if not new_sharks[(nr, nc)]:
                    new_sharks[(nr, nc)] = [shark, d]
                else:
                    if shark < new_sharks[(nr, nc)][0]:
                        new_sharks[(nr, nc)] = [shark, d]
                break

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

    changed_sharks = defaultdict(list)
    for position in new_sharks:
        shark = new_sharks[position][0]
        direction = new_sharks[position][1]
        changed_sharks[shark] = [position[0], position[1], direction]

    return changed_sharks


def reduce_smell():
    new_smells = defaultdict(list)

    for position in smells:
        if smells[position]:
            smells[position][1] -= 1
            if smells[position][1]:
                new_smells[position] = smells[position][:]

    return new_smells


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
current_directions = list(map(int, input().split()))
sharks = defaultdict(list)
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            sharks[arr[i][j]] = [i, j, current_directions[arr[i][j]-1]]

shark_directions = defaultdict(list)
for i in range(1, M+1):
    shark_directions[i] = [list(map(int, input().split())) for _ in range(4)]

smells = defaultdict(list)

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