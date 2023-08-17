import sys
from collections import deque
input = sys.stdin.readline

def convert_hexadecimal(num):
    left = str(num // 16) if num // 16 <= 9 else chr(num // 16 + 55)
    right = str(num % 16) if num % 16 <= 9 else chr(num % 16 + 55)
    return left + right

def run_incode(same_cnt, current):
    global answer

    while same_cnt > 130:
        answer += convert_hexadecimal(255) + current
        same_cnt -= 130
    if same_cnt >= 3:
        answer += convert_hexadecimal(128 + same_cnt - 3) + current
    else:
        answer += convert_hexadecimal(same_cnt - 1)
        for i in range(same_cnt):
            answer += current


def prefix_incode(queue):
    global answer

    queue_size = len(queue)
    while queue_size > 128:
        answer += convert_hexadecimal(127)
        for i in range(128):
            answer += queue.popleft()
        queue_size = len(queue)
    if queue:
        answer += convert_hexadecimal(queue_size - 1)
        for i in range(queue_size):
            answer += queue.popleft()


P = int(input())
for _ in range(P):
    B = int(input())
    data = ""
    for _ in range((B - 1) // 40 + 1):
        data += input().rstrip()

    size = len(data)    
    idx = 0
    same_cnt = 1
    queue = deque()
    answer = ""
    while idx + 1 < size:
        current = data[idx: idx + 2]
        queue.append(current)
        if idx + 2 == size:
            if same_cnt >= 3:
                run_incode(same_cnt, current)
            else:
                prefix_incode(queue)
            break
        next = data[idx + 2: idx + 4]

        if current == next:
            same_cnt += 1
            if same_cnt == 3:
                for _ in range(2):
                    queue.pop()
                prefix_incode(queue)
                queue = deque()
        else:
            if same_cnt >= 3:
                run_incode(same_cnt, current)
                queue = deque()
            same_cnt = 1
        idx += 2

    print(len(answer) // 2)
    for i in range(0, len(answer), 80):
        print(answer[i:i + 80])
