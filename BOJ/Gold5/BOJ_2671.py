# 100~인지 확인하는 함수
def is_100(sound, idx):
    global answer

    # 10000...00에서 끝나면 실패
    if answer == 'SUBMARINE' or idx == len(string):
        return

    # 이번 인덱스가 1이면
    if string[idx] == '1':
        # 아직 빈 문자열이면 1인 상태로 100~에 해당하는지 확인
        if not sound:
            is_100('1', idx+1)
        # 문자열이 있다면
        else:
            # 100~이 맞으면 (1, 10이 아닌 경우만) 100~1~로 보내기
            if len(sound) >= 3 and sound[-1] == '0' and sound[-2] == '0':
                is_1001('1', idx+1)

    # 이번 인덱스가 0이면
    elif string[idx] == '0':
        # 문자열이 있다면 100~에 0 합치기
        if sound:
            is_100(sound+'0', idx+1)


# 100~1~인지 확인하는 함수
def is_1001(sound, idx):
    global answer

    # 만약 100~1~에서 마지막 인덱스에 도달했다면 조건을 만족
    if answer == 'SUBMARINE' or idx == len(string):
        answer = 'SUBMARINE'
        return

    # 이번 인덱스가 1이면
    if string[idx] == '1':
        # 100~1~에 1연장시켜서 다음 인덱스로
        is_1001(sound + '1', idx+1)
        # 새로운 100~ 시작
        is_100('1', idx+1)

    # 이번 인덱스가 0이면 01의 시작인지도 확인
    elif string[idx] == '0':
        is_01('0', idx+1)


# 01인지 확인하는 함수
def is_01(sound, idx):
    global answer
    # 여기서 sound는 무조건 0이다.

    # 마지막 문자열이 0에서 끝났다면 종료
    if answer == 'SUBMARINE' or idx == len(string):
        return

    # 이번 인덱스가 1이면
    if string[idx] == '1':
        # 마지막으로 끝나는 패턴이 01이면 조건 만족
        if idx == len(string) - 1:
            answer = 'SUBMARINE'
            return
        # 다음 인덱스부터 100~을 만족하는지 확인하러 보내기
        is_100('', idx+1)
        # 다음 인덱스부터 01을 만족하는지 확인하러 보내기
        if idx + 1 < len(string) and string[idx+1] == '0':
            is_01('0', idx+2)


string = input()
# 조건을 만족하는 경우가 없다면 실패
answer = 'NOISE'
# 일단 100이 맞는지 확인
is_100('', 0)
# 처음 문자가 0인 경우만 01인지 확인
if string[0] == '0':
    is_01('0', 1)
print(answer)

