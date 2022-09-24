testcase = int(input())

for tc in range(testcase):
    N = int(input())
    parent = [0] * (N+1) # 인덱스 맞추기

    for _ in range(N-1):
        p, c = map(int, input().split())
        parent[c] = p # 자식 인덱스는 부모를 가리키도록

    n1, n2 = map(int, input().split())
    n1_ancestor = [n1] # 1번 노드의 조상 목록
    n2_ancestor = [n2] # 2번 노드의 조상 목록

    while True:
        if n1 in n2_ancestor: # 1번 노드가 2번 노드 조상 목록에 있다면,
            result = n1 # 1번 노드를 출력
            break
        if n2 in n1_ancestor:
            result = n2
            break
				
		# 아직 서로 겹치는 조상이 없다면,
        n1 = parent[n1] # 부모 노드로 이동
        n1_ancestor.append(n1) # 조상 목록에 추가
        n2 = parent[n2]
        n2_ancestor.append(n2)

    print(result)