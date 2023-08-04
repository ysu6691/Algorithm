import sys
input = sys.stdin.readline

N = int(input())

acc = 1
for i in range(1, N + 1):
    acc *= i

acc = str(acc)
answer = 0
for i in range(len(acc)):
    if acc[len(acc) - i - 1] != "0":
        break
    answer += 1
else:
    answer = 0

print(answer)
