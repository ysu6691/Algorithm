import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque([(N, 0)])
visited = set()
current = N
max_limit = K + 2
time = 0

while current != K:
    current, time = queue.popleft()

    if K in {current - 1, current + 1, current * 2}:
        time += 1
        break

    if current - 1 not in visited and current - 1 >= 0:
        visited.add(current - 1)
        queue.append((current - 1, time + 1))
    if current + 1 not in visited and current + 1 < max_limit:
        visited.add(current + 1)
        queue.append((current + 1, time + 1))
    if current * 2 not in visited and current * 2 < max_limit:
        visited.add(current * 2)
        queue.append((current * 2, time + 1))

print(time)
