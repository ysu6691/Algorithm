def solution(commands):

    # (r, c)의 모든 부모를 value로 변경
    def update(r, c, value):
        arr[r][c] = value
        if (r, c) != parent[r][c]:
            update(parent[r][c][0], parent[r][c][1], value)

    # (r, c)의 루트 좌표 찾기
    def find_set(r, c):
        if (r, c) == parent[r][c]:
            return r, c
        return find_set(parent[r][c][0], parent[r][c][1])

    # (r2, c2) 그룹을 (r1, c1) 그룹에 병합
    def merge(r1, c1, r2, c2):
        arr[r2][c2] = arr[r1][c1]
        if (r2, c2) != parent[r2][c2]:
            merge(r1, c1, parent[r2][c2][0], parent[r2][c2][1])
        else:
            # (r2, c2) 그룹의 루트 노드의 부모는 (r1, c1) 그룹의 리프 노드로
            parent[r2][c2] = (r1, c1)

    # (r1, c1) 그룹의 모든 노드의 리프 노드를 (r2, c2) 그룹의 리프 노드로
    def make_leaf(r1, c1, r2, c2):
        leaf[r1][c1] = leaf[r2][c2]
        if (r1, c1) != parent[r1][c1]:
            make_leaf(parent[r1][c1][0], parent[r1][c1][1], r2, c2)

    # 병합 해제
    def unmerge(r, c, target_r, target_c):
        # 리프 노드와 부모 노드 모두 자신으로 변경
        leaf[r][c] = (r, c)
        parent_r, parent_c = parent[r][c]
        parent[r][c] = (r, c)
        # 타겟 좌표만 놔두고 나머지 빈 칸으로
        if r != target_r or c != target_c:
            arr[r][c] = ''
        if (r, c) != (parent_r, parent_c):
            unmerge(parent_r, parent_c, target_r, target_c)

    answer = []
    arr = [['' for _ in range(50)] for _ in range(50)]
    parent = [[(r, c) for c in range(50)] for r in range(50)]
    leaf = [[(r, c) for c in range(50)] for r in range(50)]

    for command in commands:
        input_data = command.split()

        if input_data[0] == 'UPDATE':
            if len(input_data) == 3:
                value1 = input_data[1]
                value2 = input_data[2]
                for r in range(50):
                    for c in range(50):
                        if arr[r][c] == value1:
                            arr[r][c] = value2

            elif len(input_data) == 4:
                r, c = int(input_data[1]) - 1, int(input_data[2]) - 1
                value = input_data[3]
                r, c = leaf[r][c]
                update(r, c, value)

        elif input_data[0] == 'MERGE':
            r1, c1 = int(input_data[1]) - 1, int(input_data[2]) - 1
            r2, c2 = int(input_data[3]) - 1, int(input_data[4]) - 1
            # 같은 그룹이면 병합 x
            if find_set(r1, c1) == find_set(r2, c2):
                continue
            r1, c1 = leaf[r1][c1]
            r2, c2 = leaf[r2][c2]

            # (r1, c1)에 값이 있거나 둘 다 비워져 있으면 (r1, c1) 쪽으로 병합
            if arr[r1][c1] or not arr[r2][c2]:
                make_leaf(r1, c1, r2, c2)
                merge(r1, c1, r2, c2)
            # (r2, c2)에만 값이 있으면 (r2, c2) 쪽으로 병합
            elif arr[r2][c2]:
                make_leaf(r2, c2, r1, c1)
                merge(r2, c2, r1, c1)

        elif input_data[0] == 'UNMERGE':
            target_r, target_c = int(input_data[1]) - 1, int(input_data[2]) - 1
            r, c = leaf[target_r][target_c]
            unmerge(r, c, target_r, target_c)

        elif input_data[0] == 'PRINT':
            r, c = int(input_data[1]) - 1, int(input_data[2]) - 1
            if arr[r][c]:
                answer.append(arr[r][c])
            else:
                answer.append('EMPTY')

    return answer