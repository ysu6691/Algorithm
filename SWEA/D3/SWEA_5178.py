# 트리 만드는 함수 (후위 순회)
def make_tree(n):

    # n이 가능한 범위에 있다면,
    if 0 < n <= N:
        make_tree(n*2) # 왼쪽 자식으로
        make_tree(n*2+1) # 오른쪽 자식으로
        
        # 원래 노드
        if n in leaf_dict: # 만약 리프노드라면, 
            tree[n] = leaf_dict[n] # tree의 해당 노드에 값 저장
        else: # 만약 리프노드가 아니라면,
            if n * 2 + 1 <= N: # 오른쪽 자식이 있다면,
                tree[n] = tree[n*2] + tree[n*2+1] # 자기 자신 = 왼쪽 자식 + 오른쪽 자식
            else: # 오른쪽 자식이 없고 왼쪽 자식만 있다면,
                tree[n] = tree[n*2] # 자기 자신 = 왼쪽 자신

testcase = int(input())

for tc in range(1, testcase+1):
    N, M, L = map(int, input().split())

    # 리프 노드에 대한 정보를 담을 딕셔너리 생성
    leaf_dict = {}

    for _ in range(M):
        node, value = map(int, input().split())
        leaf_dict[node] = value # 노드에 해당하는 값 저장
    # ex) leaf_dict = {4: 1, 5: 2, 3: 3}

    tree = [0] * (N+1)
    make_tree(1) # 트리의 루트 노드는 1부터 시작

    print(f'#{tc} {tree[L]}')
