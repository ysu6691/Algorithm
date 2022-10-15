# L과 R의 각 자리를 숫자에 붙이면서 L과 R 사이에 있는 숫자가 있는지 찾기
# ex) L = 2890, R = 3041, num = 2
#     depth = 1) 가능한 num: 28, 20
#     depth = 2) 가능한 num: 289, 284, 209, 204
#     depth = 3) 가능한 num: 2890, 2891 ,... <- 사이에 있는 값 찾음 
def check(num, order):
    global success
    # 백트래킹
    if success:
        return

    if L <= num <= R: # L과 R 사이에 있는 숫자를 찾았다면 성공
        success = True
        return

    if num > R: # R보다 커졌다면 종료
        return

    if order >= len(str(R)): # R보다 자릿수가 커지면 종료
        return
    elif order >= len(str(L)): # L보다 자릿수가 커지면 R에 있는 숫자만 보기
        check(int(str(num) + str(R)[order]), order + 1)
    else: # 아직 L과 R보다 자릿수가 작다면, 두 경우 모두 생각
        check(int(str(num) + str(L)[order]), order + 1)
        check(int(str(num) + str(R)[order]), order + 1)

#############################################################

testcase = int(input())

for tc in range(1, testcase+1):
    L, R, Q = map(int, input().split())
    num_list = list(map(int, input().split()))
    answer = ''

    for i in range(Q):
        # R보다 크면 X
        if num_list[i] > R:
            answer += 'X'
        # L과 R 사이면 O
        elif L <= num_list[i] <= R:
            answer += 'O'
        # L보다 작으면 조건 고려
        else:
            # 숫자의 길이가 L과 R의 길이와 같다면, X
            if len(str(num_list[i])) == len(str(L)) and len(str(num_list[i])) == len(str(R)):
                answer += 'X'
            # 숫자의 길이가 L과 R보다 작다면, 재귀 돌리기
            else:
                success = False
                check(num_list[i], len(str(num_list[i])))
                if success:
                    answer += 'O'
                else:
                    answer += 'X'

    print(f'#{tc} {answer}')
