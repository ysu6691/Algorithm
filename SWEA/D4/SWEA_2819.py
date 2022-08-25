def perm(depth):
    if depth == 6:
        move_list.append(selection[:])
        return

    for i in range(4):
        check[i] = 1
        selection[depth] = move[i]
        perm(depth+1)
        check[i] = 0

testcase = int(input())

for tc in range(1, testcase+1):

    arr = [list(map(int, input().split())) for _ in range(4)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    move = [0, 1, 2, 3]

    move_list = []
    check = [0] * 4
    selection = [0] * 6

    num_set = set()

    perm(0)

    for i in range(4):
        for j in range(4):
            for p in move_list:
                tmp = str(arr[i][j])
                ny = i
                nx = j
                for q in p:
                    nx += dx[q]
                    ny += dy[q]

                    if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                        tmp = str(arr[i][j])
                        ny = i
                        nx = j
                        break

                    tmp += str(arr[ny][nx])

                if len(tmp) == 7:
                    num_set.add(tmp)

    print(f'#{tc} {len(num_set)}')