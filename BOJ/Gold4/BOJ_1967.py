import sys
input = sys.stdin.readline

n = int(input())
parent = [(1, 0) for _ in range(n + 1)]
children_cnt = [0] * (n + 1)

leaves = set(range(1, n + 1))
for _ in range(n - 1):
    p, c, cost = map(int, input().split())
    parent[c] = (p, cost)
    children_cnt[p] += 1
    leaves.discard(p)

stack = list(leaves)
distance = [0] * (n + 1)
answer = 0

while stack:
    current = stack.pop()
    if current == 1:
        continue
    answer = max(answer, distance[parent[current][0]] + distance[current] + parent[current][1])
    distance[parent[current][0]] = max(distance[parent[current][0]], distance[current] + parent[current][1])
    children_cnt[parent[current][0]] -= 1
    if not children_cnt[parent[current][0]]:
        stack.append(parent[current][0])

print(answer)