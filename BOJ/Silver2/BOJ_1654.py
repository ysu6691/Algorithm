import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

lines.sort()

left = 1
right = 2 ** 31 - 1
max_length = -1

while left <= right:
    middle = (left + right) // 2
    cnt = 0
    for line in lines:
        cnt += line // middle
    if cnt >= N and middle > max_length:
        max_length = middle
        left = middle + 1
    else:
        right = middle - 1

print(max_length)