# 지역나누기
def split_area(x, y, d1, d2, direction):

    # 범위 벗어나면 백트래킹
    if x + d1 + d2 >= N or y + d2 >= N or y - d1 < 0:
        return

    # 지역 합 계산 후 답 갱신하기
    sum_area(x, y, d1, d2)

    # 상,우 방향으로 늘리기
    if direction == 1:
        split_area(x, y, d1+1, d2, 1) # 그대로 가기
        split_area(x, y, d1, d2+1, 2) # 방향 변경
    # 하,우 방향으로 늘리기
    elif direction == 2:
        split_area(x, y, d1, d2+1, 2)


# 지역 합 계산 후 답 갱신
def sum_area(x, y, d1, d2):
    global answer
    area1, area2, area3, area4, area5 = 0, 0, 0, 0, 0
    area5_set = {(x, y)}
    nx, ny = x, y
    tmp_arr = [[0]*N for _ in range(N)]

    # 경계선 그리기
    # 각 방향으로 이동하면서 가상 좌표에 표시하고 좌표 기억하기
    for i in range(d1):
        nx += 1
        ny -= 1
        area5_set.add((nx, ny))
        tmp_arr[ny][nx] = 1
    for i in range(d2):
        nx += 1
        ny += 1
        area5_set.add((nx, ny))
        tmp_arr[ny][nx] = 1
    for i in range(d1):
        nx -= 1
        ny += 1
        area5_set.add((nx, ny))
        tmp_arr[ny][nx] = 1
    for i in range(d2):
        nx -= 1
        ny -= 1
        area5_set.add((nx, ny))
        tmp_arr[ny][nx] = 1

    # 2차원 배열을 돌면서 경계선 내부 채우기
    for r in range(N):
        for c in range(N):
            if tmp_arr[r][c]:
                tmp_set = set()
                flag = False
                while True:
                    c += 1
                    if c == N:
                        break
                    tmp_set.add((c, r))
                    if tmp_arr[r][c]:
                        flag = True
                        break
                if flag:
                    area5_set |= tmp_set
                break

    # 각 지역 조건에 맞게 합 계산
    for r in range(N):
        for c in range(N):
            if r < y and c <= x + d1 and (c, r) not in area5_set:
                area1 += arr[r][c]
            elif r <= y - d1 + d2 and c > x + d1 and (c, r) not in area5_set:
                area2 += arr[r][c]
            elif r >= y and c < x + d2 and (c, r) not in area5_set:
                area3 += arr[r][c]
            elif r > y - d1 + d2 and c >= x + d2 and (c, r) not in area5_set:
                area4 += arr[r][c]
            else:
                area5 += arr[r][c]
    
    # 최대 최소 구하기
    max_area = max(area1, area2, area3, area4, area5)
    min_area = min(area1, area2, area3, area4, area5)
    if max_area - min_area < answer:
        answer = max_area - min_area


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 987654321

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for y in range(N):
    for x in range(N):
        # 모든 좌표에서부터 경계선 그리기 시작 (d1, d2, direction은 1부터)
        split_area(x, y, 1, 1, 1)
print(answer)