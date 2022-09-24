def maketree(idx, depth):
    if 0 < idx < 2**K and depth < K:
        tree[depth].append(visited[idx])
        maketree(idx-2**(K-depth-2), depth+1)
        maketree(idx+2**(K-depth-2), depth+1)

K = int(input())
visited = [0]
visited += list(map(int, input().split()))
tree = [[] for _ in range(K)]
maketree(2**(K-1), 0)

for i in range(K):
    print(' '.join(map(str, tree[i])))
