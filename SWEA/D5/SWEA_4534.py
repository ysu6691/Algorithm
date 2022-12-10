from collections import deque

testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    children = [0]*(N+1)
    parent = [0]*(N+1)
    adj_matrix = [[] for _ in range(N+1)]
    for _ in range(N-1):
        n1, n2 = map(int, input().split())
        adj_matrix[n1].append(n2)
        adj_matrix[n2].append(n1)

    stack = [1]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            for destination in adj_matrix[current]:
                if destination not in visited:
                    parent[destination] = current
                    children[current] += 1
                    stack.append(destination)

    color_list = [[1, 1] for _ in range(N+1)]

    queue = deque()
    for idx in range(N, 0, -1):
        if not children[idx]:
            queue.append(idx)
    while queue:
        current = queue.popleft()
        color_list[parent[current]][0] *= color_list[current][0] + color_list[current][1]
        color_list[parent[current]][1] *= color_list[current][0]

        children[parent[current]] -= 1
        if not children[parent[current]]:
            queue.append(parent[current])

    print(f'#{tc} {(color_list[1][0] + color_list[1][1]) % 1000000007}')