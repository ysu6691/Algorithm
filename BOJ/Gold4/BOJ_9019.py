import sys
from collections import deque
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    A, B = map(str, input().split())

    queue = deque([(A, "")])
    memo = {A}

    while queue:
        current, string = queue.popleft()
        
        nextD = str((int(current) * 2) % 10000)
        if nextD == B:
            print(string + "D")
            break
        nextS = str(int(current) - 1 if int(current) > 0 else 9999)
        if nextS == B:
            print(string + "S")
            break
        nextL = str(int(current[1:] + current[0])) if len(current) == 4 else current + "0"
        if nextL == B:
            print(string + "L")
            break
        nextR = str(int(current[-1] + current[:-1])) if len(current) == 4 else str(int(current[-1] + "0" * (4 - len(current)) + current[:-1]))
        if nextR == B:
            print(string + "R")
            break

        if nextD not in memo:
            memo.add(nextD)
            queue.append((nextD, string + "D"))
        if nextS not in memo:
            memo.add(nextS)
            queue.append((nextS, string + "S"))   
        if nextL not in memo:
            memo.add(nextL)
            queue.append((nextL, string + "L"))
        if nextR not in memo:
            memo.add(nextR)
            queue.append((nextR, string + "R"))
