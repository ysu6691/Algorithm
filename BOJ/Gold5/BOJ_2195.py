# 현재 인덱스부터 몇 칸만큼 갈 수 있는지 확인
def check(sidx, pidx):
    global cnt
    # 맞는 문자열 수 세기
    tmp_cnt = 0
    while True:
        # 인덱스 벗어나거나 문자열이 서로 맞지 않으면,
        # 지금 확인하고 있는 패턴이 최대만큼 갔는지 확인
        if sidx >= len_S or pidx >= len_P or S[sidx] != P[pidx]:
            if tmp_cnt > cnt:
                cnt = tmp_cnt
            return
        sidx += 1
        pidx += 1
        tmp_cnt += 1


S = input()
P = input()
len_S = len(S)
len_P = len(P)

pidx = 0
answer = 0
while True:
    answer += 1
    cnt = 0
    # S 돌면서 현재 P 인덱스와 같은 문자열 발견하면 함수 실행
    for sidx in range(len_S):
        if S[sidx] == P[pidx]:
            check(sidx, pidx)
    # 인덱스 이동
    pidx += cnt
    if pidx >= len_P:
        break

print(answer)