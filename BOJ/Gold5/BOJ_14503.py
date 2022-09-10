N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향(d)에 따라 이동할 방향 설정 (0번째 인덱스부터 우선순위)
# ex) d = 1(동쪽): 북, 서, 남, 동 순으로 탐색
dr = [[0, 1, 0, -1], [-1, 0, 1, 0], [0, -1, 0, 1], [1, 0, -1, 0]]
dc = [[-1, 0, 1, 0], [0, -1, 0, 1], [1, 0, -1, 0], [0, 1, 0, -1]]

# 원래 보고 있던 방향과 몇 번 회전했는지에 따라, 현재 보고 있는 방향 맞추기
# ex) 초기에 d = 1이었고 3번 회전했다면, 나중 d = change[1][2]
change = [[3, 2, 1, 0], [0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3]]

cnt = 0

while True:
    # 현재 위치가 0이면 2로 바꾸기 (청소하기)
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1

    # 현재 위치가 1이면 청소 끝내기 (후진하다가 만난 경우)
    if arr[r][c] == 1:
        break

    # 현재 보고 있는 방향에서 왼쪽으로 돌면서 0이 있는지 확인
    for i in range(4):
        if arr[r + dr[d][i]][c + dc[d][i]] == 0:
            r += dr[d][i]
            c += dc[d][i]
            d = change[d][i] # 방향 재설정
            break
    else:
        # 0이 없다면 뒤로 후진
        r += dr[d][1]
        c += dc[d][1]

print(cnt)