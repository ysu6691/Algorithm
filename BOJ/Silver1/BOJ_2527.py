for _ in range(4):

    rectangles = list(map(int, input().split()))

    rec1 = rectangles[:4]
    rec2 = rectangles[4:]

    result = 0

    if rec1[0] > rec2[2] or rec1[1] > rec2[3]:
        result = 'd'
    elif rec2[0] > rec1[2] or rec2[1] > rec1[3]:
        result = 'd'

    elif rec1[0] == rec2[2] and rec1[1] == rec2[3]:
        result = 'c'
    elif rec2[0] == rec1[2] and rec2[1] == rec1[3]:
        result = 'c'
    elif rec1[0] == rec2[2] and rec1[3] == rec2[1]:
        result = 'c'
    elif rec2[0] == rec1[2] and rec2[3] == rec1[1]:
        result = 'c'

    elif rec1[0] == rec2[2] or rec1[1] == rec2[3]:
        result = 'b'
    elif rec2[0] == rec1[2] or rec2[1] == rec1[3]:
        result = 'b'

    else:
        result = 'a'

    print(result)