N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 경사로를 실제로 2차원 배열에 놓기
# 행과 열에 놓는 경사로를 따로 생각하므로, 각각 따로 생성
slope_arr_row = [[0]*N for _ in range(N)]
slope_arr_col = [[0]*N for _ in range(N)]

# check = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# check[0] = 행
# check[1] = 열
# 만약 3행이 조건을 만족하지 않는다면, check[0][2] = 0
# 2차원 배열을 모둗 돌고 난 뒤, check[0]과 check[1]의 원소를 모두 더하면 가능한 길의 개수가 됨
check = [[1]*N, [1]*N]

# 왼쪽에서 오른쪽으로 커지는 경사로 놓기
for i in range(N):
    cnt = 1  # 같은 높이의 길이 얼마만큼 있는지 세기
    flag = False

    # 만약 해당 행이 이미 조건을 만족하지 않았다면, 다음 행으로 건너뛰기
    if not check[0][i]:
        continue

    for j in range(N-1):
        # 만약 다음 칸이 이전 칸보다 1보다 크게 차이가 난다면, 다음 행으로
        if arr[i][j+1] - arr[i][j] > 1:
            check[0][i] = 0
            break

        # 만약 다음 칸과 이전 칸이 1만큼 차이난다면, if문 통과
        elif arr[i][j+1] - arr[i][j] == 1:

            # 만약 같은 높이의 길보다 경사로의 길이가 더 길다면, 다음 행으로
            if cnt < L:
                check[0][i] = 0
                break
                
            else:
                # 만약 경사로를 놓았을 때 2차원 배열 안에 있다면, if문 통과
                if j - L + 1 >= 0:
                    # 경사로 길이만큼 이전 칸을 보면서,
                    # 만약 이미 경사로를 놓았다면, 다음 행으로
                    for k in range(L):
                        if slope_arr_row[i][j-k] == 1:
                            check[0][i] = 0
                            flag = True
                            break
                        # 경사로 놓기
                        slope_arr_row[i][j-k] = 1
                    # 다음 칸부터 높이가 달라지므로, cnt 리셋
                    cnt = 0
                    
                # 경사로가 2차원 배열을 넘어서면, 다음 행으로
                else:
                    check[0][i] = 0
                    break
                    
        # 만약 다음 칸의 높이가 더 낮다면, cnt 리셋 (반대 방향은 다른 for문에서 확인)
        elif arr[i][j] > arr[i][j+1]:
            cnt = 0

        if flag:
            break

        cnt += 1

for i in range(N):
    cnt = 1
    flag = False
    if not check[0][i]:
        continue
    for j in range(N-1, 0, -1):
        if arr[i][j-1] - arr[i][j] > 1:
            check[0][i] = 0
            break
        elif arr[i][j-1] - arr[i][j] == 1:
            if cnt < L:
                check[0][i] = 0
                break
            else:
                if j + L - 1 < N:
                    for k in range(L):
                        if slope_arr_row[i][j+k] == 1:
                            check[0][i] = 0
                            flag = True
                            break
                        slope_arr_row[i][j+k] = 1
                    cnt = 0
                else:
                    check[0][i] = 0
                    break
        elif arr[i][j-1] > arr[i][j]:
            cnt = 0
        if flag:
            break
        cnt += 1

for i in range(N):
    cnt = 1
    flag = False
    if not check[1][i]:
        continue
    for j in range(N-1):
        if arr[j+1][i] - arr[j][i] > 1:
            check[1][i] = 0
            break
        elif arr[j+1][i] - arr[j][i] == 1:
            if cnt < L:
                check[1][i] = 0
                break
            else:
                if j - L + 1 >= 0:
                    for k in range(L):
                        if slope_arr_col[j-k][i] == 1:
                            check[1][i] = 0
                            flag = True
                            break
                        slope_arr_col[j-k][i] = 1
                    cnt = 0
                else:
                    check[1][i] = 0
                    break
        elif arr[j][i] > arr[j+1][i]:
            cnt = 0
        if flag:
            break
        cnt += 1

for i in range(N):
    cnt = 1
    flag = False
    if not check[1][i]:
        continue
    for j in range(N-1, 0, -1):
        if arr[j-1][i] - arr[j][i] > 1:
            check[1][i] = 0
            break
        elif arr[j-1][i] - arr[j][i] == 1:
            if cnt < L:
                check[1][i] = 0
                break
            else:
                if j + L - 1 < N:
                    for k in range(L):
                        if slope_arr_col[j+k][i] == 1:
                            check[1][i] = 0
                            flag = True
                            break
                        slope_arr_col[j+k][i] = 1
                    cnt = 0
                else:
                    check[1][i] = 0
                    break
        elif arr[j-1][i] > arr[j][i]:
            cnt = 0
        if flag:
            break
        cnt += 1

print(sum(check[0]) + sum(check[1]))