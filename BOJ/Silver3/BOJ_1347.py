# '#'로 구성된 100x100 행렬 만들기
# [50, 50]에서 시작
# 입력 받은대로 움직이면서 '.'남기고, 최대 최소 좌표 저장
# 다 움직인 후, 최소 좌표부터 최대 좌표까지 출력

def maze(direction, x, y):
    global max_x, max_y, min_x, min_y

    # 다 움직였다면, 함수 종료
    if len(move_list) == 0:
        return

    # 맨 처음 값 받아오기
    move = move_list.pop(0)

    # direction = 0(남), 1(서), 2(북), 3(동)

    # 왼쪽으로 전환
    if move == 'L':
        direction -= 1
        if direction == -1:
            direction = 3

    # 오른쪽으로 전환
    elif move == 'R':
        direction += 1
        if direction == 4:
            direction = 0

    # 앞으로 이동
    elif move == 'F':
        if direction == 0:
            y += 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x += 1
        map[y][x] = '.'

        # 최대, 최소 좌표 저장
        if x > max_x:
            max_x = x
        elif x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        elif y < min_y:
            min_y = y

    # 다음 행동하기
    maze(direction, x, y)


N = int(input())
move_list = list(input())
map = [['#']*100 for _ in range(100)]
map[50][50] = '.' # 맨 처음 좌표 찍기

max_x = 50
min_x = 50
max_y = 50
min_y = 50

maze(0, 50, 50)

for i in range(min_y, max_y+1):
    print(''.join(map[i][min_x : max_x+1]))
