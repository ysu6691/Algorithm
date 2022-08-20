# 아이디어
# 숫자를 부를 때마다, 빙고판에 해당 숫자를 0으로 바꾸기
# 숫자 부를 때마다 빙고판 확인해, 가로, 세로, 대각선의 합이 0인지 확인 

# 빙고판 생성
arr = [list(map(int, input().split())) for _ in range(5)]

# 심판이 부르는 숫자 순서대로 저장
call_list = []

for _ in range(5):
    call_list.extend(list(map(int, input().split())))

cnt = 0

# 숫자 부를 때마다 빙고판에서 해당 자리 0으로 바꾸기
# 그리고나서 가로, 세로, 대각선 각각 합이 0인지 확인
# 합이 0인 것이 세 개 이상이면, 출력 후 break
for number in call_list:
    bingo = 0
    break_for = False
    for i in range(5):
        for j in range(5):
            if number == arr[i][j]:
                arr[i][j] = 0
                cnt += 1
                break_for = True # 해당 숫자 찾았다면, 이중 포문 파괴
                break
        if break_for:
            break

    for i in range(5):
        check_row = 0
        check_col = 0
        for j in range(5):
            check_row += arr[i][j]
            check_col += arr[j][i]

        if not check_row:
            bingo += 1
        if not check_col:
            bingo += 1

    if arr[0][0] + arr[1][1] + arr[2][2] + arr[3][3] + arr[4][4] == 0:
        bingo += 1
    if arr[4][0] + arr[3][1] + arr[2][2] + arr[1][3] + arr[0][4] == 0:
        bingo += 1

    if bingo >= 3:
        print(cnt)
        break

