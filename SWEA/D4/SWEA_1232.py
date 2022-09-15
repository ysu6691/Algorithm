# 계산하는 함수
def calc(n):
    if n:
        calc(left[n]) # 왼쪽으로
        calc(right[n]) # 오른쪽으로

        # 만약 n이 리프노드가 아니라면, 저장했던 연산자에 맞게 계산
        if n in not_leaf:
            if not_leaf[n] == '+':
                tree[n] = tree[left[n]] + tree[right[n]]
            elif not_leaf[n] == '-':
                tree[n] = tree[left[n]] - tree[right[n]]
            elif not_leaf[n] == '*':
                tree[n] = tree[left[n]] * tree[right[n]]
            elif not_leaf[n] == '/':
                tree[n] = tree[left[n]] // tree[right[n]]

for tc in range(1, 11):
    N = int(input())
    not_leaf = {}
    tree = [0] * (N+1)

    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        node_info = list(input().split())

        # 리프노드가 아니라면,
        if len(node_info) == 4:
            not_leaf[int(node_info[0])] = node_info[1]    # 딕셔너리에 해당 연산자 저장
            left[int(node_info[0])] = int(node_info[2])   # 왼쪽 자식 노드 저장
            right[int(node_info[0])] = int(node_info[3])  # 오른쪽 자식 노드 저장

        # 리프노드라면,
        else:
            tree[int(node_info[0])] = int(node_info[1]) # 주어진 값 저장

    # not_leaf = {1: '-', 2: '-'}
    # tree = [0, 0, 0, 10, 88, 65]

    # 루트노드는 1
    calc(1)
    # tree = [0, 13, 23, 10, 88, 65]

    print(f'#{tc} {tree[1]}')
