import sys, heapq
from collections import deque
input = sys.stdin.readline

import heapq

testcase = int(input())
for _ in range(testcase):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    queue = deque()
    for i in range(N):
        queue.append((num_list[i], i))
    sorted_list = sorted(num_list)

    cnt = 1
    while queue:
        max_num = sorted_list.pop()
        while True:
            current, idx = queue.popleft()
            if current == max_num:
                break
            queue.append((current, idx))

        if idx == M:
            break
        cnt += 1
        
    print(cnt)
