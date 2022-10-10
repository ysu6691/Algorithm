import copy

# 벽돌 떨어뜨리는 함수
def drop(idx, n, arr):
    tmp_arr = copy.deepcopy(arr)

    # N번만큼 떨어뜨렸다면, 남은 벽돌 세기
    if n == N:
        global min_cnt
        cnt = 0
        for i in range(H):
            for j in range(W):
                if tmp_arr[i][j]:
                    cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt
        return

    # 현재 위치에서 떨어뜨렸을때, 첫 번째로 만나는 벽돌 높이 구하기
    height = 0
    while height < H:
        if tmp_arr[height][idx]:
            num = tmp_arr[height][idx] # 그 때의 벽돌 숫자 저장
            break
        height += 1

    # 만약 중간에 벽돌을 만나지 않고 끝까지 도달했다면,
    # 남은 벽돌이 더 이상 없는건지 확인
    if height == H:
        for i in range(H):
            for j in range(W):
                if tmp_arr[i][j]: # 남은 벽돌이 아직 있다면,
                    return # 백트래킹
        min_cnt = 0 # 더이상 남은 벽돌이 없다면, 최솟값 0으로 갱신
        return

    # 벽돌 숫자만큼 터뜨리기
    explosion(height, idx, num, tmp_arr)

    # 터뜨린 뒤 공중에 떠있는 벽돌 내리기
    for i in range(W):
        for j in range(H-1, -1, -1):
            if not tmp_arr[j][i]:
                k = j - 1
                while k >= 0:
                    if tmp_arr[k][i]:
                        tmp_arr[j][i] = tmp_arr[k][i]
                        tmp_arr[k][i] = 0
                        break
                    k -= 1

    # 다음 벽돌 떨어뜨리기
    for i in range(W):
        drop(i, n+1, tmp_arr)

# 폭파시키는 함수
def explosion(r, c, num, tmp_arr):
    # 일단 현재 위치부터 터뜨리기
    tmp_arr[r][c] = 0

    # 현재 벽돌 숫자만큼 상하좌우 터뜨리기
    for i in range(num):
        for j in range(4):
            nr = r + dr[j] * i
            nc = c + dc[j] * i

            if 0 <= nr < H and 0 <= nc < W:
                if tmp_arr[nr][nc] == 1: # 1이라면 함수 안 들어가고 그냥 0으로 바꾸기
                    tmp_arr[nr][nc] = 0
                elif tmp_arr[nr][nc]: # 다른 숫자라면 연쇄 폭발
                    explosion(nr, nc, tmp_arr[nr][nc], tmp_arr)

#####################################################################3

testcase = int(input())

for tc in range(1, testcase+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    min_cnt = 12 * 15 + 1

    # 0 ~ W-1 번째 인덱스까지 벽돌 차례대로 떨어뜨리기
    for i in range(W):
        drop(i, 0, arr)

    print(f'#{tc} {min_cnt}')