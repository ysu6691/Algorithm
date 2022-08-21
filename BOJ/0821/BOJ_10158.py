# 시간초과
# w, h = map(int, input().split())
#
# current = list(map(int, input().split()))
#
# t = int(input())
#
# move = [1, 1]
#
# for _ in range(t):
#     for i in range(2):
#         current[i] += move[i]
#
#     if current[0] == w:
#         move[0] = -1
#     elif current[0] == 0:
#         move[0] = 1
#
#     if current[1] == h:
#         move[1] = -1
#     elif current[1] == 0:
#         move[1] = 1
#
# print(current[0], current[1])


w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

# 벽에 부딪히는지 확인
# 벽에 안 부딪힌다면, 그대로 좌표에 더하기
if t <= w - p:
    x = p + t

# 벽에 부딪힌다면, new_t 생성
else:
    new_t = t - (w - p)

    # new_t가 홀수면(오른쪽으로 이동하고 있다면),
    # 그때의 좌표 계산
    if (new_t // w) % 2:
        x = new_t % w

    # new_t가 짝수면(왼쪽으로 이동하고 있다면),
    # 그때의 좌표 계산
    else:
        x = w - (new_t % w)

# y좌표도 동일하게 적용
if t <= h - q:
    y = q + t
else:
    new_t = t - (h - q)
    if (new_t // h) % 2:
        y = new_t % h
    else:
        y = h - (new_t % h)

print(x, y)