testcase = int(input())

for tc in range(1, testcase+1):

    p, q = map(int, input().split())

    arr = [[0] * 300 for i in range(300)]

    num = 1

    p_x = 0
    p_y = 0
    q_x = 0
    q_y = 0

    for i in range(1, 300):
        arr[i][1] = num
        num += i
        if p == arr[i][1]:
            p_x = 1
            p_y = i
        if q == arr[i][1]:
            q_x = 1
            q_y = i

    for i in range(1, 300):
        for j in range(2, 300):
            arr[i][j] = arr[i][j-1] + i + j - 1
            if p == arr[i][j]:
                p_x = j
                p_y = i
            if q == arr[i][j]:
                q_x = j
                q_y = i

    new_x = p_x + q_x
    new_y = p_y + q_y

    print(f'#{tc} {arr[new_y][new_x]}')
