# 큐 사용
from collections import deque

N = int(input())
indegree = [0] * (N + 1)
parent_graph = [[] for i in range(N + 1)] # 자신이 향하는 노드를 담을 배열
child_graph = [[] for i in range(N + 1)] # 자신에게 향하는 노드를 남을 배열
times = [0] * (N + 1) # 각 노드의 시간을 담을 리스트

for i in range(1, N+1):
    info = list(map(int, input().split()))
    times[i] = info[0] # 시간 저장
    for j in range(1, len(info) - 1):
        parent_graph[info[j]].append(i) # 자신이 향하는 노드를 담기
        child_graph[i].append(info[j]) # 자신에게 향하는 노드를 담기
        indegree[i] += 1 # 차수 증가

# parent_graph = [[], [2, 3, 4], [], [4, 5], [], []]
# child_graph = [[], [], [1], [1], [3, 1], [3]]

# 위상 정렬
def topology_sort():
    q = deque()
    current = 0

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in parent_graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
								# 차수가 0이 됐을 때, 자신에게 향하는 노드 시간 중 가장 큰 시간 더하기
                max_time = 0
                for j in child_graph[i]:
                    if times[j] > max_time:
                        max_time = times[j]
                times[i] += max_time

topology_sort()
for i in range(1, N+1):
    print(times[i])