from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_positions = [] # 바이러스 좌표 저장
num_virus = 0 # 바이러스 수 저장
num_blank = 0 # 빈 칸 수 저장
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus_positions.append((i, j))
            num_virus += 1
        elif arr[i][j] == 0:
            num_blank += 1

# M개 좌표 조합 모두 저장
virus_position_comb = []
for i in range(1 << num_virus):
    tmp = []
    for j in range(num_virus):
        if i & (1 << j):
            tmp.append(virus_positions[j])
    if len(tmp) == M:
        virus_position_comb.append(tmp)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 987654321

# 모든 조합에 대해 BFS 수행
for virus_positions in virus_position_comb:
    queue = deque(virus_positions)
    visited = set()
    time = -1
    flag = False
    cnt = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                # 찾은 빈 칸 수 세기
                if not arr[current[0]][current[1]]:
                    cnt += 1
                for i in range(4):
                    nr = current[0] + dr[i]
                    nc = current[1] + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited and arr[nr][nc] in {0, 2}:
                        queue.append((nr, nc))

        time += 1
        # 빈 칸 모두 찾았다면 break
        if cnt == num_blank:
            break
        # 백트래킹
        if time >= answer:
            flag = True
            break

    # 정답 갱신
    if not flag and cnt == num_blank:
        answer = time

if answer == 987654321:
    answer = -1

print(answer)