import copy

def move(arr, direction, cnt):
    tmp_arr = copy.deepcopy(arr)

    if cnt == 6:
        global max_num
        for i in range(N):
            for j in range(N):
                if tmp_arr[i][j] > max_num:
                    max_num = tmp_arr[i][j]
        return

    if direction == 'up':
        for i in range(N):
            for j in range(N):
                if tmp_arr[j][i]:
                    k = j+1
                    while k < N:
                        if tmp_arr[k][i]:
                            if tmp_arr[j][i] == tmp_arr[k][i]:
                                tmp_arr[j][i] += tmp_arr[k][i]
                                tmp_arr[k][i] = 0
                            break
                        k += 1

                    k = 0
                    while k < j:
                        if tmp_arr[k][i] == 0:
                            tmp_arr[k][i] = tmp_arr[j][i]
                            tmp_arr[j][i] = 0
                        k += 1

    elif direction == 'down':
        for i in range(N):
            for j in range(N-1, -1, -1):
                if tmp_arr[j][i]:
                    k = j-1
                    while k >= 0:
                        if tmp_arr[k][i]:
                            if tmp_arr[j][i] == tmp_arr[k][i]:
                                tmp_arr[j][i] += tmp_arr[k][i]
                                tmp_arr[k][i] = 0
                            break
                        k -= 1

                    k = N-1
                    while k > j:
                        if tmp_arr[k][i] == 0:
                            tmp_arr[k][i] = tmp_arr[j][i]
                            tmp_arr[j][i] = 0
                        k -= 1

    elif direction == 'left':
        for i in range(N):
            for j in range(N):
                if tmp_arr[i][j]:
                    k = j+1
                    while k < N:
                        if tmp_arr[i][k]:
                            if tmp_arr[i][j] == tmp_arr[i][k]:
                                tmp_arr[i][j] += tmp_arr[i][k]
                                tmp_arr[i][k] = 0
                            break
                        k += 1

                if tmp_arr[i][j]:
                    k = 0
                    while k < j:
                        if tmp_arr[i][k] == 0:
                            tmp_arr[i][k] = tmp_arr[i][j]
                            tmp_arr[i][j] = 0
                        k += 1

    elif direction == 'right':
        for i in range(N):
            for j in range(N-1, -1, -1):
                if tmp_arr[i][j]:
                    k = j-1
                    while k >= 0:
                        if tmp_arr[i][k]:
                            if tmp_arr[i][j] == tmp_arr[i][k]:
                                tmp_arr[i][j] += tmp_arr[i][k]
                                tmp_arr[i][k] = 0
                            break
                        k -= 1
                if tmp_arr[i][j]:
                    k = N-1
                    while k > j:
                        if tmp_arr[i][k] == 0:
                            tmp_arr[i][k] = tmp_arr[i][j]
                            tmp_arr[i][j] = 0
                        k -= 1

    move(tmp_arr, 'up', cnt+1)
    move(tmp_arr, 'down', cnt+1)
    move(tmp_arr, 'left', cnt+1)
    move(tmp_arr, 'right', cnt+1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_num = -1
move(arr, 'up', 1)
move(arr, 'down', 1)
move(arr, 'left', 1)
move(arr, 'right', 1)
print(max_num)