# 중위 순회
def inorder(n):
    if n:
        inorder(c1[n])
        char_list.append(V[n])
        inorder(c2[n])

for tc in range(1, 11):

    N = int(input())

    V = [0] * (N+1) # 각 노드의 문자를 담을 리스트
    c1 = [0] * (N+1) # 왼쪽 자식
    c2 = [0] * (N+1) # 오른쪽 자식

    for i in range(N):
        input_list = list(input().split())
        
        p = int(input_list[0]) # 부모 노드
        V[p] = input_list[1] # 노드의 문자

        # 왼쪽 자식까지 알려줬다면, 왼쪽 자식 추가
        if len(input_list) == 3:
            c1[p] = int(input_list[2])

        # 오른쪽 자식까지 알려줬다면, 자식 둘 다 추가
        if len(input_list) == 4:
            c1[p] = int(input_list[2])
            c2[p] = int(input_list[3])

    char_list = []
    inorder(1)
    result = ''.join(char_list)

    print(f'#{tc} {result}')