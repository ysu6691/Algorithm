def find_set(n):
    if n != parent[n]:
        n = find_set(parent[n])
    return parent[n]

def union(n1, n2):
    n1 = find_set(n1)
    n2 = find_set(n2)
    if rank[n1] > rank[n2]:
        parent[n2] = n1
    elif rank[n2] > rank[n1]:
        parent[n1] = n2
    else:
        parent[n2] = n1
        rank[n1] += 1

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = list(range(N+1))
rank = [0]*(N+1)
total_cost = 0
cnt = 0

for edge in edges:
    n1, n2, cost = edge[0], edge[1], edge[2]

    if find_set(n1) != find_set(n2):
        union(n1, n2)
        total_cost += cost
        cnt += 1
        if cnt == N - 2:
            break

print(total_cost)