# 순열 만들기
def perm(depth):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        flag = False
        if not check[i]:
            check[i] = 1
            selection[depth] = arr[i]
            # 대각선에 이미 선택한 말이 있는지 확인
            for j in range(depth):
                if abs(selection[j] - selection[depth]) == depth - j: # 이미 있다면,
                    check[i] = 0 # 백트래킹
                    flag = True
                    break
            if flag:
                continue
            perm(depth+1)
            check[i] = 0

testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    arr = [i for i in range(N)]
    check = [0] * N
    selection = [100] * N

    cnt = 0

    perm(0)

    print(f'#{tc} {cnt}')

