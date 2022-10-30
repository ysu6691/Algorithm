N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향을 알면, 어느 좌표의 idx번째 인덱스가 비율이 몇 인지 알 수 있다.
ratio_list = [1, 1, 7, 7, 2, 2, 10, 10, 5]
ratio_direction = {
    # key: 방향 / value: 방향
    0: [(-1, 0), (1, 0), (-1, -1), (1, -1), (-2, -1), (2, -1), (-1, -2), (1, -2), (0, -3)],
    1: [(0, -1), (0, 1), (1, -1), (1, 1), (1, -2), (1, 2), (2, -1), (2, 1), (3, 0)],
    2: [(-1, 0), (1, 0), (-1, 1), (1, 1), (-2, 1), (2, 1), (-1, 2), (1, 2), (0, 3)],
    3: [(0, -1), (0, 1), (-1, -1), (-1, 1), (-1, -2), (-1, 2), (-2, -1), (-2, 1), (-3, 0)]
}

# 토네이도 카운트만큼 이동하면서 돌기
# ex) N = 5
#     count = [1, 1, 2, 2, 3, 3, 4, 4, 4]
count = []
for i in range(1, N):
    count.append(i)
    count.append(i)
count.append(N-1)

# 시작은 정중앙
r = N // 2
c = N // 2

# 방향은 좌, 하, 우, 상 순서로
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

answer = 0
direction = 0
idx = 0
# 밖으로 나가면서 돌기
while True:
    cnt = count[idx]
    while cnt:
        acc = 0
        # nr, nc 는 y좌표
        nr = r + dr[direction]
        nc = c + dc[direction]
        # 9개의 비율이 적혀있는 칸 확인
        for i in range(9):
            rr = r + ratio_direction[direction][i][0]
            rc = c + ratio_direction[direction][i][1]

            # 배열 안에 있다면, 비율만큼 더하기
            if 0 <= rr < N and 0 <= rc < N:
                arr[rr][rc] += int(arr[nr][nc] * ratio_list[i] / 100)
            # 배열 밖에 있다면, 답 누적
            else:
                answer += int(arr[nr][nc] * ratio_list[i] / 100)
            # 감소한 모래 누적
            acc += int(arr[nr][nc] * ratio_list[i] / 100)

        # 알파 좌표
        remain_r = r + dr[direction] * 2
        remain_c = c + dc[direction] * 2
        # 알파 좌표가 배열 안에 있다면 알파 좌표에 모래 누적
        if 0 <= remain_r < N and 0 <= remain_c < N:
            arr[remain_r][remain_c] += arr[nr][nc] - acc
        # 알파 좌표가 배열 밖에 있다면 정답 누적
        else:
            answer += arr[nr][nc] - acc
        
        # y좌표의 모래는 0으로
        arr[nr][nc] = 0
        # 다음 좌표로
        r += dr[direction]
        c += dc[direction]
        cnt -= 1

    idx += 1
    direction += 1
    if direction == 4:
        direction = 0
    if idx == len(count):
        break

print(answer)