import sys
import heapq

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        weight, current = heapq.heappop(heap)
        if not visited[current]:
            visited[current] = 1
            distance[current] = weight

        for i in adj_list[current]:
            if not visited[i] and adj_matrix[current][i] + distance[current] < distance[i]:
                heapq.heappush(heap, (adj_matrix[current][i] + distance[current], i))

def reasonable(current):
    if DP[current]:
        return DP[current]

    for destination in adj_list[current]:
        if distance[destination] < distance[current]:
            DP[current] += reasonable(destination)

    return DP[current]


input = sys.stdin.readline
N, M = map(int, input().split())
INF = 987654321
adj_matrix = [[INF]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
distance = [INF]*(N+1)
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2, w = map(int, input().split())
    adj_matrix[n1][n2] = w
    adj_matrix[n2][n1] = w
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

dijkstra(2)

DP = [0]*(N+1)
DP[2] = 1
reasonable(1)

print(DP[1])