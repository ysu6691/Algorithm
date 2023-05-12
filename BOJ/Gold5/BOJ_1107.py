import sys
input = sys.stdin.readline

def find_answer(num):
    global answer

    if len(str(num)) == 6:
        return

    for i in alive_buttons:
        tmp = str(num)
        tmp += str(i)
        if abs(N - int(tmp)) + len(str(int(tmp))) < answer:
            answer = abs(N - int(tmp)) + len(str(int(tmp)))
        if int(tmp):
            find_answer(int(tmp))

N = int(input())
M = int(input())
broken_buttons = set(map(int, input().split()))
alive_buttons = []
for i in range(10):
    if i not in broken_buttons:
        alive_buttons.append(i)

answer = abs(N - 100)
for i in alive_buttons:
    if abs(N - i) + 1 < answer:
        answer = abs(N - i) + 1
    if i:
        find_answer(i)

print(answer)