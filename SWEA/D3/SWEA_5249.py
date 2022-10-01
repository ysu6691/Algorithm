def find_set(n):
    if n != parent[n]:
        n = find_set(parent[n])
    return parent[n]

def union(n1, n2):
    n1 = find_set(n1)
    n2 = find_set(n2)

    # parent[n2] = n1
    if rank[n1] > rank[n2]:
        parent[n2] = n1
    elif rank[n2] > rank[n1]:
        parent[n1] = n2
    else:
        parent[n2] = n1
        rank[n1] += 1

testcase = int(input())

for tc in range(1, testcase+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key=lambda x: x[2])
    rank = [0] * (V+1)
    parent = list(range(V+1))
    tmp = 0

    answer = 0
    cnt = 0
    for edge in edges:
        n1, n2, w = edge[0], edge[1], edge[2]

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            answer += w
            cnt += 1

            if cnt == V:
                break

    print(f'#{tc} {answer}')