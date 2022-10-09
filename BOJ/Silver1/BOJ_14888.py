# pypy에서만 시간초과 x
N = int(input())
N_list = list(map(int, input().split()))
operators = list(map(int, input().split()))
operators_list = [] # 연산자를 숫자로 담을 리스트
# +: 0, -: 1, *: 2, /: 3

for i in range(4):
    for j in range(operators[i]):
        operators_list.append(i)
# ex) operators_list = [0, 0, 1, 2, 3]

check = [0]*(N-1)
selection = [0]*(N-1)
max_acc = -1000000001
min_acc = 1000000001

# 순열로 연산자를 숫자 사이에 끼워 넣기
def perm(depth):
    if depth == N-1:
        global max_acc, min_acc
        tmp = selection[:] # <- 그냥 selection으로 해도 됨
        acc = N_list[0]
        # 연산자에 맞게 연산
        for i in range(1, N):
            if tmp[i-1] == 0:
                acc += N_list[i]
            elif tmp[i-1] == 1:
                acc -= N_list[i]
            elif tmp[i-1] == 2:
                acc *= N_list[i]
            elif tmp[i-1] == 3:
                acc = int(acc / N_list[i])
        # 최대, 최소 확인
        if acc > max_acc:
            max_acc = acc
        if acc < min_acc:
            min_acc = acc
        return

    for i in range(N-1):
        if not check[i]:
            check[i] = 1
            selection[depth] = operators_list[i]
            perm(depth+1)
            check[i] = 0

perm(0)

print(max_acc)
print(min_acc)

##########################################################
# python에서도 시간초과 x
N = int(input())
N_list = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_acc = -1000000001
min_acc = 1000000001

# DFS
def calc(acc, idx, plus, minus, multi, devision):
    
    # 끝까지 도달했다면, 최댓값 혹은 최솟값 갱신
    if idx == N:
        global max_acc, min_acc
        if acc > max_acc:
            max_acc = acc
        if acc < min_acc:
            min_acc = acc

    # 현재 연산자에 맞게 연산
    if plus:
        calc(acc+N_list[idx], idx+1, plus-1, minus, multi, devision)
    if minus:
        calc(acc-N_list[idx], idx+1, plus, minus-1, multi, devision)
    if multi:
        calc(acc*N_list[idx], idx+1, plus, minus, multi-1, devision)
    if devision:
        calc(int(acc/N_list[idx]), idx+1, plus, minus, multi, devision-1)

# 연산 시작
calc(N_list[0], 1, operators[0], operators[1], operators[2], operators[3])

print(max_acc)
print(min_acc)