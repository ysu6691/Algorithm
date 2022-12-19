problem = input()
answer = ''
group = ''
memo = -1
cnt = 1
flag = False

for idx in range(len(problem)):
    # 콜론 만났을 때
    if problem[idx] == ':':
        # ::의 뒤에 위치한 콜론인 경우 넘기기
        if flag:
            flag = False
            continue
        
        # ::의 앞에 위치한 콜론인 경우 몇 번째 콜론인지 기억 
        if idx <= len(problem) - 2 and problem[idx+1] == ':':
            memo = cnt
            flag = True # 뒤에 오는 콜론은 넘기기
        
        # 0 부족한만큼 채워서 답에 추가하기
        group = '0' * (4 - len(group)) + group
        answer += ':' + group
        group = '' # 채운 다음 다시 빈 상태로
        cnt += 1 # 콜론 기억
        
    # 콜론 외 다른 모든 문자열은 그룹에 추가
    else:
        group += problem[idx]

# 맨 뒤에 4자리도 마저 채우기
answer += ':' + '0' * (4 - len(group)) + group
answer = answer[1:]

# :: 사이 0000으로 채우기
while memo >= 0 and len(answer) < 39:
    answer = answer[:memo*5 - 1] + ':0000:' + answer[memo*5:]

print(answer)