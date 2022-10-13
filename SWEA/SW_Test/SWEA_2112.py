def insert_drug(sidx, count, arr):
    global answer
    if count >= answer:
        return

    if sidx == D:
        if check_pass(arr):
            answer = count
        return

    tmp_row = arr[sidx][:]
    insert_drug(sidx+1, count, arr)
    arr[sidx] = [0]*W
    insert_drug(sidx+1, count+1, arr)
    arr[sidx] = [1]*W
    insert_drug(sidx+1, count+1, arr)
    arr[sidx] = tmp_row[:]

def check_pass(arr):
    if K == 1:
        return True
    for i in range(W):
        current = arr[0][i]
        cnt = 1
        for j in range(1, D):
            if arr[j][i] == current:
                cnt += 1
                if cnt >= K:
                    break
            else:
                current = arr[j][i]
                cnt = 1
        else:
            return False
    return True


testcase = int(input())

for tc in range(1, testcase+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    answer = D
    insert_drug(0, 0, arr)

    print(f'#{tc} {answer}')