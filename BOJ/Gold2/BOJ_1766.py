import heapq

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

queue = []
visited = set()

for i in range(1, N+1):
    if not indegree[i]:
        queue.append(i)

answer = []

while queue:
    current = heapq.heappop(queue)

    if current not in visited:
        visited.add(current)
        answer.append(current)

        for next in graph[current]:
            if next not in visited and indegree[next]:
                indegree[next] -= 1
                if not indegree[next]:
                    heapq.heappush(queue, next)

print(' '.join(map(str, answer)))