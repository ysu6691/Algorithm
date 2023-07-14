import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2, cost = map(int, input().split())
    adj_list[n1].append((cost, n2))
    adj_list[n2].append((cost, n1))

INF = 1000001
distance = [INF] * (N + 1)
queue = [(0, 1)]
visited = [0] * (N + 1)
distance[1] = 0

while queue:
    cost, current = heapq.heappop(queue)
    if visited[current]:
        continue
    visited[current] = 1
    for adj_info in adj_list[current]:
        if not visited[adj_info[1]] and adj_info[0] < distance[adj_info[1]]:
            distance[adj_info[1]] = adj_info[0]
            heapq.heappush(queue, (adj_info[0], adj_info[1]))
    
print(sum(distance[1:]) - max(distance[1:]))