# 사각형이 겹치는 경우를 찾는게 까다로울 것 같아서,
# 안 겹치는 경우, 꼭짓점 하나가 겹치는 경우, 선분이 겹치는 경우 순으로 찾아내기

for _ in range(4):

    rectangles = list(map(int, input().split()))

    # 각 사각형 좌표 저장
    rec1 = rectangles[:4]
    rec2 = rectangles[4:]

    result = 0

    # 서로 겹칠 수가 없는 경우
    if rec1[0] > rec2[2] or rec1[1] > rec2[3]:
        result = 'd'
    elif rec2[0] > rec1[2] or rec2[1] > rec1[3]:
        result = 'd'

    # 꼭짓점 하나가 겹치는 경우
    elif rec1[0] == rec2[2] and rec1[1] == rec2[3]:
        result = 'c'
    elif rec2[0] == rec1[2] and rec2[1] == rec1[3]:
        result = 'c'
    elif rec1[0] == rec2[2] and rec1[3] == rec2[1]:
        result = 'c'
    elif rec2[0] == rec1[2] and rec2[3] == rec1[1]:
        result = 'c'

    # 사각형의 x좌표 혹은 y좌표가 하나라도 겹치는 경우
    # (꼭짓점 하나가 겹치는 경우는 위에서 제외했으므로, 선분이 겹치는 경우밖에 없음)
    elif rec1[0] == rec2[2] or rec1[1] == rec2[3]:
        result = 'b'
    elif rec2[0] == rec1[2] or rec2[1] == rec1[3]:
        result = 'b'

    # 다 걸러내고 남은건 사각형이 겹치는 경우밖에 없음
    else:
        result = 'a'

    print(result)