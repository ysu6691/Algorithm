# BFS 이용
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

result = 64

di = [1, 0]
dj = [0, 1]

for i in range(N-7):
    for j in range(M-7):
        queue = [(i, j, 0)]
        visited = []
        cnt = 0
        check = 0

        while queue:
            current = queue.pop(0)
            if (current[0], current[1]) not in visited:
                check += 1
                visited.append((current[0], current[1]))
                if current[2] % 2 == 0:
                    if arr[current[0]][current[1]] != arr[i][j]:
                        cnt += 1
                else:
                    if arr[current[0]][current[1]] == arr[i][j]:
                        cnt += 1

                for k in range(2):
                    ni = current[0] + di[k]
                    nj = current[1] + dj[k]

                    if ni < i+8 and nj < j+8:
                        if (ni, nj) not in visited:
                            queue.append((ni, nj, current[2]+1))

        if cnt < result:
            result = cnt
        if 64 - cnt < result:
            result = 64 - cnt

print(result)

###########################################

# 이중 FOR문 이용
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

result = 64

for i in range(N-7):
    for j in range(M-7):
        cnt = 0

        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if (r - i) % 2 == (c - j) % 2:
                    if arr[r][c] != arr[i][j]:
                        cnt += 1
                if (r - i) % 2 != (c - j) % 2:
                    if arr[r][c] == arr[i][j]:
                        cnt += 1

        if cnt < result:
            result = cnt
        if 64 - cnt < result:
            result = 64 - cnt

print(result)