def find_set(n):
    if n != parent[n]:
        n = find_set(parent[n])
    return parent[n]

def union(n1, n2):
    n1 = find_set(n1)
    n2 = find_set(n2)
    parent[n2] = n1

testcase = int(input())

for tc in range(1, testcase+1):
    N, M = map(int, input().split())
    parent = list(range(N+1))
    students = list(map(int, input().split()))

    for i in range(M):
        n1, n2 = students[i*2], students[i*2+1]
        if find_set(n1) != find_set(n2):
            union(n1, n2)

    for i in range(1, N+1):
        parent[i] = find_set(parent[i])

    print(f'#{tc} {len(set(parent))-1}')