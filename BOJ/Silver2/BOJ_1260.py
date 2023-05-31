import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

stack = [V]
stack_memo = []
visited = set()
while stack:
    current = stack.pop()
    if current in visited:
        continue

    stack_memo.append(current)
    visited.add(current)

    candidate = []
    for destination in adj_list[current]:
        if destination not in visited:
            candidate.append(destination)

    stack.extend(sorted(candidate, reverse=True))

queue = deque([V])
queue_memo = []
visited = set()

while queue:
    current = queue.popleft()
    if current in visited:
        continue

    queue_memo.append(current)
    visited.add(current)

    candidate = []
    for destination in adj_list[current]:
        if destination not in visited:
            candidate.append(destination)

    queue.extend(sorted(candidate))

print(" ".join(map(str, stack_memo)))
print(" ".join(map(str, queue_memo)))