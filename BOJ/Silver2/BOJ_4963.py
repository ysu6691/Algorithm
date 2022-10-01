# 상하좌우와 대각선을 모두 DFS 수행

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]

    # 상하좌우 + 대각선
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, 1, -1, 1, -1]

    visited = set()
    answer = 0

    for i in range(h):
        for j in range(w):
            # 이미 방문하지 않은 섬을 찾았다면 DFS 수행
            if arr[i][j] == 1 and (i, j) not in visited:
                stack = [(i, j)]
                answer += 1

                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add((current[0], current[1]))

                        for k in range(8): # 8방향 모두 보기
                            ni = current[0] + di[k]
                            nj = current[1] + dj[k]

                            if 0 <= ni < h and 0 <= nj < w:
                                if arr[ni][nj] and (ni, nj) not in visited:
                                    stack.append((ni, nj))

    print(answer)