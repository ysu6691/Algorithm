from collections import deque, defaultdict
import heapq, math


def solution(land, height):
    def find_parent(n):
        if parent[n] != n:
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
            if n1 < n2:
                parent[n2] = n1
                rank[n1] += 1
            else:
                parent[n1] = n2
                rank[n2] += 1

    N = len(land)
    parent = [[-1] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if parent[r][c] != -1:
                continue
            queue = deque([(r, c)])
            parent[r][c] = cnt
            while queue:
                current = queue.popleft()
                for i in range(4):
                    nr = current[0] + dr[i]
                    nc = current[1] + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and parent[nr][nc] == -1 and abs(
                            land[current[0]][current[1]] - land[nr][nc]) <= height:
                        queue.append((nr, nc))
                        parent[nr][nc] = cnt
            cnt += 1

    adj_dict = dict()
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and parent[r][c] != parent[nr][nc]:
                    current_num = parent[r][c]
                    adj_num = parent[nr][nc]
                    gap = abs(land[nr][nc] - land[r][c])
                    if (current_num, adj_num) in adj_dict:
                        adj_dict[(current_num, adj_num)] = min(adj_dict[(current_num, adj_num)], gap)
                    else:
                        adj_dict[(current_num, adj_num)] = gap

    adj_dict = sorted(adj_dict.items(), key=lambda x: x[1])
    parent = list(range(cnt))
    rank = [0] * cnt
    edges = []
    for (n1, n2), cost in adj_dict:
        edges.append((cost, n1, n2))
    edges.sort()
    answer = 0
    for edge in edges:
        cost, n1, n2 = edge
        n1 = find_parent(n1)
        n2 = find_parent(n2)
        if n1 != n2:
            union(n1, n2)
            answer += cost

    return answer
