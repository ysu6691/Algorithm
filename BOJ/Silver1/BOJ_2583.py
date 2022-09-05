# 2차원 리스트에 사각형 채우기
# MxN 행렬을 돌면서, 빈 칸이 있다면 DFS 수행 -> 경로 지나면서 빈 칸은 1로 메꾸기

M, N, K = map(int, input().split())

arr = [[0]*N for _ in range(M)]

# 좌표받아와서, 2차원 리스트에 사각형 채우기
for _ in range(K):
    point1_x, point1_y, point2_x, point2_y = map(int, input().split())

    for i in range(point1_y, point2_y):
        for j in range(point1_x, point2_x):
            arr[i][j] = 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

cnt_list = []

# MxN을 돌면서, 빈칸이 있다면 DFS 수행
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            stack = [(i, j)]
            cnt = 0

            while stack:
                current = stack.pop()
                if arr[current[0]][current[1]] == 0:
                    arr[current[0]][current[1]] = 1
                    cnt += 1

                    for k in range(4):
                        ni = current[0] + di[k]
                        nj = current[1] + dj[k]

                        if 0 <= ni < M and 0 <= nj < N:
                            if arr[ni][nj] == 0:
                                stack.append((ni, nj))

            # 빈 칸을 다 메꿨다면, 그 때의 빈칸 개수 저장
            cnt_list.append(cnt)

print(len(cnt_list))
print(' '.join(map(str, sorted(cnt_list))))


