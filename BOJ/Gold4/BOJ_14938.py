import heapq

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
INF = 987654321
graph = [[] for _ in range(n+1)]

for i in range(r):
    node1, node2, length = map(int, input().split())
    graph[node1].append([node2, length])
    graph[node2].append([node1, length])

total_cnt = 0

def dijkstra(start):
    global total_cnt

    queue = [(0, start)]
    distance = [INF] * (n + 1)
    distance[start] = 0
    cnt = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > m:
            break

        if distance[node] < dist:
            continue

        cnt += items[node]

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(queue, (cost, next[0]))

    if cnt > total_cnt:
        total_cnt = cnt

for i in range(1, n+1):
    dijkstra(i)

print(total_cnt)