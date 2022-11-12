from collections import defaultdict

testcase = int(input())

for tc in range(1, testcase+1):
    croaks = input()
    frogs = defaultdict(list)
    cnt = 1 # 개구리 번호 매기기
    croak_dict = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a', 'c': 'k'}

    for s in croaks:
        # 받은 문자열이 c면,
        if s == 'c':
            # 낮은 번호 개구리부터 보기
            for frog in frogs:
                # 만약 다음 울음을 시작할 수 있는 개구리가 있다면, 또 울기
                if not frogs[frog]:
                    frogs[frog] = ['c']
                    break
            # 모든 개구리가 울고 있다면 새로운 개구리 추가 
            else:
                frogs[cnt] = ['c']
                cnt += 1
            continue

        # 받은 문자열이 c가 아니면, 해당 문자열이 들어갈 수 있는 개구리 찾기
        before = croak_dict[s]
        # 마찬가지로 낮은 번호 개구리부터 보기
        for frog in frogs:
            # 해당 문자열에 맞는 개구리가 있다면, 문자열 추가
            if frogs[frog] and frogs[frog][-1] == before:
                frogs[frog].append(s)
                # 만약 울음 사이클이 끝났다면, 빈 배열로 만들기(c 받을 준비)
                if s == 'k':
                    frogs[frog] = []
                break
        # 만약 해당하는 문자열을 받을 수 있는 개구리가 없다면, -1 출력
        else:
            answer = -1
            break
    else:
        answer = len(frogs)
        for frog in frogs:
            # 울다 만 개구리가 있다면 -1 출력
            if frogs[frog] or not answer:
                answer = -1
                break

    print(f'#{tc} {answer}')