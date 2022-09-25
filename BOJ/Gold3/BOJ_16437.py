N = int(input())
parent = [0]*(N+1)
animal_info = [0]*(N+1)
result = 0

for i in range(N-1):
    info = input().split()
    # 양이면, 양의 수와 부모 노드 저장
    if info[0] == 'S':
        animal_info[i+2] = int(info[1])
        parent[i+2] = int(info[2])
    # 늑대면, 늑대 수를 음수로 저장하고 부모 노드는 그대로 저장
    else:
        animal_info[i+2] = -int(info[1])
        parent[i+2] = int(info[2])

for i in range(2, N+1):
    # 2번 노드부터 아래로 돌기 (늑대가 없는 경로면 바로 1번 노드로 보내기 위해)
    if animal_info[i] > 0: # 양이면 while문 시작
        node = i
        num = animal_info[i]
        start = i
        while True:
            if node == 1: # 1번 노드면 그때의 양 수 저장
                result += num
                parent[start] = 1 # 시작점에서 1번 노드까지는 안전한 길임
                break
            if node > 1: # 1번 노드가 아닐 때
                if animal_info[parent[node]] >= 0: # 부모 노드가 양이면,
                    node = parent[node] # 부모 노드로 이동
                else: # 부모 노드가 늑대면,
                    if -animal_info[parent[node]] >= num: # 늑대 수가 현재 양 수보다 많다면,
                        animal_info[parent[node]] += num # 그만큼 늑대 수 줄이기
                        break
                    else: # 늑대 수가 현재 양 수보다 적다면,
                        tmp = -animal_info[parent[node]]
                        animal_info[parent[node]] = 0 # 늑대 0으로 만들기
                        node = parent[node] # 부모 노드로 이동
                        num -= tmp # 줄어든 양 수 만큼 가지고 가기
                        parent[start] = node # 시작점에서 현재 노드까지는 안전함

print(result)