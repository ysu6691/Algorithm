# 90도 회전
def rotate(L):
    # 빈 배열에 넣기
    tmp_arr = [[0]*n for _ in range(n)]
    # 격자로 나누기
    for r in range(0, n, 2**L):
        for c in range(0, n, 2**L):
            # 숫자 집어넣기
            c_cnt = 0
            for i in range(r, r+2**L):
                r_cnt = 1
                for j in range(c, c+2**L):
                    tmp_arr[i][j] = arr[r+2**L - r_cnt][c + c_cnt]
                    r_cnt += 1
                c_cnt += 1
    return tmp_arr


# 얼음 녹이기
def reduce():
    # 빈 배열에 넣기
    tmp_arr = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            # 얼음이 없는 곳은 건너뛰기
            if not arr[r][c]:
                continue
            # 주변에 얼음이 세 칸 미만으로 있다면, 1 감소
            cnt = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < n and arr[nr][nc]:
                    cnt += 1
            if cnt < 3:
                tmp_arr[r][c] = arr[r][c] - 1
            else:
                tmp_arr[r][c] = arr[r][c]
    return tmp_arr

##################################################################

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))
n = 2**N # 배열 길이 저장

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for L in L_list:
    arr = rotate(L)
    arr = reduce()

# 얼음 합 구하기
acc = 0
for r in range(n):
    for c in range(n):
        acc += arr[r][c]

# 가장 큰 덩어리 구하기
max_cnt = 0
visited = set()
for r in range(n):
    for c in range(n):
        if arr[r][c] and (r, c) not in visited:
            stack = [(r, c)]
            tmp_cnt = 0

            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    tmp_cnt += 1

                    for k in range(4):
                        nr = current[0] + dr[k]
                        nc = current[1] + dc[k]

                        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc]:
                            stack.append((nr, nc))

            if tmp_cnt > max_cnt:
                max_cnt = tmp_cnt

print(acc)
print(max_cnt)