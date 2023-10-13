import sys
input = sys.stdin.readline

N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

stack = [1]
visited = [0] * (N + 1)
visited[1] = 1

parent = list(range(N + 1))

while stack:
    current = stack.pop()
    for dest in adj_list[current]:
        if not visited[dest]:
            parent[dest] = current
            stack.append(dest)
            visited[dest] = 1

for i in range(2, N + 1):
    sys.stdout.write(str(parent[i]) + "\n")
sys.stdout.flush()
