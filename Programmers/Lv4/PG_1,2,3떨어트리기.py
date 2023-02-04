def solution(edges, target):

    # while문 들어가기 전에 첫 번째 리프노드를 찾는 함수
    def find_first_leaf(current):
        if current in leaves:
            return current
        return find_first_leaf(children[current][0])

    # 리프노드부터 루트노드까지 방향을 모두 바꾸는 함수
    def change_direction(current):
        current_direction_idx[current] += 1
        if current_direction_idx[current] == len(children[current]):
            current_direction_idx[current] = 0
        if current == 0:
            return
        change_direction(parent[current])

    # 방향바꾼 뒤 그 다음 리프노드를 찾는 함수
    def find_next_leaf(current):
        if current in leaves:
            return current
        return find_next_leaf(children[current][current_direction_idx[current]])

    parent = [0] * len(target)
    children = [[] for _ in range(len(target))]
    current_direction_idx = [0] * len(target)

    # parent, children 저장
    for edge in edges:
        p, c = edge[0] - 1, edge[1] - 1
        parent[c] = p
        children[p].append(c)

    # 자식노드가 있다면 노드 번호 순대로 정렬
    for node in range(len(children)):
        if not children[node]:
            continue
        children[node].sort()
        # 현재 가리키는 자식 인덱스는 가장 첫 번째 자식
        current_direction_idx[node] = 0

    # 리프 노드들 저장
    leaves = set()
    for node in range(len(target)):
        if target[node]:
            leaves.add(node)

    # 첫 리프노드 가져오기
    current_leaf = find_first_leaf(0)
    # 리프노드에 숫자가 어떻게 쌓이고 있는지 딕셔너리로 저장
    history_list = [{1: 0, 2: 0, 3: 0} for _ in range(len(target))]
    # while문 한 번마다 어떤 리프노드 차례였는지 기억
    sequence_list = []

    while True:
        history = history_list[current_leaf]
        sequence_list.append(current_leaf)

        # 현재 리프노드가 이미 목표만큼 채워졌다면 2 -> 1 + 1 or 3 -> 2 + 1로 바꿔보기
        if history[1] + history[2] * 2 + history[3] * 3 == target[current_leaf]:
            if history[2]:
                history[1] += 2
                history[2] -= 1
            elif history[3]:
                history[1] += 1
                history[2] += 1
                history[3] -= 1
            else:
                return [-1]

        # 현재 리프노드가 아직 목표만큼 채워지지 않았다면 3부터 목표 안넘치게 채워보기
        else:
            history[3] += 1
            if history[1] + history[2] * 2 + history[3] * 3 > target[current_leaf]:
                history[2] += 1
                history[3] -= 1
                if history[1] + history[2] * 2 + history[3] * 3 > target[current_leaf]:
                    history[1] += 1
                    history[2] -= 1

        # 리프노드가 모두 목표치를 채웠다면 while문 종료
        for leaf in leaves:
            history = history_list[leaf]
            if history[1] + history[2] * 2 + history[3] * 3 != target[leaf]:
                break
        else:
            break

        # 조상 노드들 방향 바꾸고 다음 리프노드로
        change_direction(current_leaf)
        current_leaf = find_next_leaf(0)

    # 리프노드마다 1, 2, 3 순서대로 얼만큼 나왔는지 채우기
    # ex) {1: 2, 2: 1, 3: 1} -> [1, 1, 2, 3]
    idx_list = [[] for _ in range(len(target))]
    for node in range(len(target)):
        if node not in leaves:
            continue
        for num in range(1, 4):
            for _ in range(history_list[node][num]):
                idx_list[node].append(num)

    # 리프노드 방문했던 순서대로 나온 숫자만큼 채우기
    answer = []
    for leaf in sequence_list:
        num = idx_list[leaf].pop(0)
        answer.append(num)

    return answer
