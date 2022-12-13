# 각 노드마다 [선정했을 때 최댓값, 선정하지 않았을 때 최댓값] 계산
# 선정했을 때 최댓값은 자식 노드가 모두 선정되지 않았을 경우 1가지이다.
# 선정하지 않았을 때 최댓값은 각 자식 노드마다 두 경우 중 최댓값을 합한 값이다.

from collections import deque

N = int(input())
people_list = list(map(int, input().split()))
adj_list = [[] for _ in range(N)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    n1 -= 1
    n2 -= 1
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

parent = [-1]*N # 부모 노드를 가리키는 리스트
children = [0]*N # 자식 수를 나타내는 리스트
stack = [0]
visited = set()

# parent와 children 리스트 채우기
while stack:
    current = stack.pop()
    if current not in visited:
        visited.add(current)

        for destination in adj_list[current]:
            if destination not in visited:
                stack.append(destination)
                children[current] += 1
                parent[destination] = current

# 리프 노드 찾아서 queue에 넣고 현재 노드 누적값 [노드 인원수, 0]으로 만들기
queue = deque()
acc_list = [[0, 0] for _ in range(N)]
for node in range(N):
    if not children[node]:
        queue.append(node)
        acc_list[node][0] = people_list[node]

while queue:
    current = queue.popleft()
    parent_node = parent[current]
    # 부모 노드가 우수마을인 경우 현재 마을이 우수마을이 아닌 경우를 누적
    acc_list[parent_node][0] += acc_list[current][1]
    # 부모 노드가 우수마을이 아닌 경우, 현재 마을의 두가지 경우 중 최댓값을 누적
    acc_list[parent_node][1] += max(acc_list[current])
    # 확인한 자식 카운트
    children[parent_node] -= 1
    # 모든 자식을 카운트했으면 queue에 넣고 자기 자신도 누적하기
    if not children[parent_node]:
        queue.append(parent_node)
        acc_list[parent_node][0] += people_list[parent_node]

print(max(acc_list[0]))