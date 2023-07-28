import sys
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N):
    adj_info = list(map(int, input().split()))[:-1]
    for i in range(1, len(adj_info), 2):
        adj_list[adj_info[0]].append((adj_info[i], adj_info[i + 1]))

parent = list(range(N + 1))
stack = [1]
visited = [0] * (N + 1)
visited[1] = 1
leaves = []
children_cnt = [0] * (N + 1)
while stack:
    current = stack.pop()
    flag = False
    for adj_info in adj_list[current]:
        if not visited[adj_info[0]]:
            parent[adj_info[0]] = (current, adj_info[1])
            stack.append(adj_info[0])
            visited[adj_info[0]] = 1
            children_cnt[current] += 1
    if not children_cnt[current]:
        leaves.append(current)

tree = [[0] for _ in range(N + 1)]
while leaves:
    current = leaves.pop()
    if current == 1:
        continue
    tree[parent[current][0]].append(max(tree[current]) + parent[current][1])
    children_cnt[parent[current][0]] -= 1
    if not children_cnt[parent[current][0]]:
        leaves.append(parent[current][0])

answer = 0
for node in range(1, N + 1):
    if len(tree[node]) > 1:
        answer = max(answer, sum(sorted(tree[node], reverse=True)[:2]))

print(answer)