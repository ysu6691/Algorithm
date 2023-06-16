import sys
input = sys.stdin.readline

def find_parent(n):
    if n != parent[n]:
        parent[n] = find_parent(parent[n])
    return parent[n]

def union(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)

    if rank[n1] > rank[n2]:
        parent[n2] = n1
    elif rank[n1] < rank[n2]:
        parent[n1] = n2
    else:
        if n1 > n2:
            parent[n2] = n1
            rank[n1] += 1
        else:
            parent[n1] = n2
            rank[n2] += 1


N, M = map(int, input().split())
parent = list(range(N + 1))
rank = [0] * (N + 1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    if find_parent(n1) != find_parent(n2):
        union(n1, n2)

answer = 0
parent_set = set()
for n in range(1, N + 1):
    if find_parent(n) not in parent_set:
        parent_set.add(parent[n])
        answer += 1

print(answer)
    
