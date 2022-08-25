testcase = int(input())

for tc in range(1, testcase+1):

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    current = [0, 0]

    matrix_list = [[n, n]]

    cnt = 0

    while True:
        if arr[current[0]][current[1]] != 0:

            cnt += 1

            start_row = current[0]
            end_row = current[0]

            while True:
                end_row += 1
                if end_row == n or arr[end_row][current[1]] == 0:
                    break

            height = end_row - start_row

            start_col = current[1]
            end_col = current[1]

            while True:
                end_col += 1
                if end_col == n or arr[current[0]][end_col] == 0:
                    break

            width = end_col - start_col

            for i in range(start_row, end_row):
                for j in range(start_col, end_col):
                    arr[i][j] = 0

            for i in range(len(matrix_list)):
                if height*width < matrix_list[i][0] * matrix_list[i][1]:
                    matrix_list.insert(i, [height, width])
                    break
                elif height*width == matrix_list[i][0] * matrix_list[i][1]:
                    if height < matrix_list[i][0]:
                        matrix_list.insert(i, [height, width])
                    else:
                        matrix_list.insert(i+1, [height, width])
                    break

        current[1] += 1

        if current[1] >= n:
            current[0] += 1
            current[1] = 0

        if current[0] >= n:
            break

    result = []

    for matrix in matrix_list:
        result.append(matrix[0])
        result.append(matrix[1])

    result = ' '.join(map(str, result))

    print(f'#{tc} {cnt} {result}')