# 지금까지 드래곤이 움직인 방향을 저장하는 리스트를 생성한다.
# 세대가 바뀔 때, 지금까지 움직였던 방향을 반대로 뒤집는다.
# 뒤집은 방향을 0 -> 1 -> 2 -> 3 -> 0 과 같이 바꿔서, 리스트에 추가한다.
# 모든 세대의 드래곤 방향을 정했으면, 리스트대로 움직이면서 2차원 배열을 그린다.

N = int(input())

arr = [[0]*101 for _ in range(101)]
move_dict = {'0': 1, '1': 2, '2': 3, '3': 0}

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 입력받는대로 2차원 배열에 그리기
for i in range(N):
    x, y, direction, generation = map(int, input().split())
    move_list = [direction] # 방향 리스트에 처음 방향 넣고 시작

    # 처음 위치 표시
    arr[y][x] = 1

    # 세대 증가
    for _ in range(generation):
        # 현재 세대 방향의 길이를 저장
        current_length = len(move_list)

        # 뒤에서부터 돌면서, 방향을 규칙에 맞게 바꿔서 추가
        for j in range(current_length-1, -1, -1):
            move_list.append(move_dict[str(move_list[j])])

    # 모든 방향을 저장한 뒤에, 저장한 대로 움직이면서 경로 그리기
    for move in move_list:
        x += dx[move]
        y += dy[move]

        arr[y][x] = 1

cnt = 0

# 네 꼭짓점이 1이라면 cnt 증가
for i in range(100):
    for j in range(100):
        if arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1] == 4:
            cnt += 1

print(cnt)