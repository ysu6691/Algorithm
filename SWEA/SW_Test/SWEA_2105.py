def move(current, direction, num_set):
    # 다시 오른쪽아래로 이동하려고 하면, 종료
    if direction == 4:
        return

    # 출발점에 다시 도달했다면, 최대 길이 갱신
    global max_acc
    if num_set and current == start:
        if len(num_set) > max_acc:
            max_acc = len(num_set)
        return

    # 배열을 벗어나면, 백트래킹
    if current[0] < 0 or current[0] >= N or current[1] < 0 or current[1] >= N:
        return

    r = current[0]
    c = current[1]

    # 이미 밟았던 번호라면, 백트래킹
    if arr[r][c] in num_set:
        return

    # 셋 id 재설정 후 현재 밟은 숫자 추가
    num_set = set(num_set)
    num_set.add(arr[r][c])

    # 1. 현재 이동 방향 그대로 계속 이동하기
    # 2. 현재 이동하는 방향 다음 방향으로 이동하기
    move([r + dr[direction], c + dc[direction]], direction, num_set)
    move([r + dr[direction], c + dc[direction]], direction + 1, num_set)

#######################################################

testcase = int(input())
for tc in range(1, testcase+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 시계방향(오른쪽아래, 왼쪽아래, 왼쪽위, 오른쪽위 방향)으로 차례대로 이동
    # (시계방향으로 돌았다면, 반시계방향으로는 돌 필요 x)
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    max_acc = -1

    # 배열을 돌면서 사각형 그려보기
    for i in range(N):
        for j in range(N):
            start = [i, j]
            move([i, j], 0, set())

    print(f'#{tc} {max_acc}')