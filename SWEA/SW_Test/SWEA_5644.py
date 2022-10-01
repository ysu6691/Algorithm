testcase = int(input())

for tc in range(1, testcase+1):
    N, BC = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    arr = [[] for _ in range(11)]
    for i in range(11):
        for j in range(11):
            arr[i].append([]) # 각 좌표에 해당하는 충전기를 모두 담기 위해 리스트로 생성

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 충전기에 해당하는 범위만큼 설치 (BFS)
    num = 1
    for i in range(BC):
        x, y, c, p = map(int, input().split())
        queue = [(y, x, 0)]
        visited = []

        while queue:
            current = queue.pop(0)
            if (current[0], current[1]) not in visited and current[2] <= c:
                visited.append((current[0], current[1]))
                arr[current[0]][current[1]].append((p, num))

                for k in range(4):
                    ny = current[0] + dy[k]
                    nx = current[1] + dx[k]

                    if 0 < nx < 11 and 0 < ny < 11 and (ny, nx) not in visited:
                        queue.append((ny, nx, current[2]+1))

        num += 1

    # A, B 이동하면서 충전
    A = [1, 1]
    B = [10, 10]
    move = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
    answer = 0
    for m in range(N+1):
        A_charge = []
        B_charge = []
        # 각자 위치에서 충전기 정보 모두 받아오기
        for i in range(len(arr[A[0]][A[1]])):
            A_charge.append(arr[A[0]][A[1]][i])
        for i in range(len(arr[B[0]][B[1]])):
            B_charge.append(arr[B[0]][B[1]][i])

        A_charge.sort(reverse=True) # 내림차순 정렬
        B_charge.sort(reverse=True)

        # 만약 A자리에 충전기가 있다면,
        if A_charge:
            first = A_charge[0]
            answer += first[0] # 일단 가장 큰 충전기부터 충전
            # 그게 B의 가장 큰 충전기와 같다면,
            if B_charge and B_charge[0] == first:
                # A, B 중 그 다음으로 큰 충전기로 충전
                if len(A_charge) > 1 and len(B_charge) > 1:
                    answer += max(A_charge[1][0], B_charge[1][0])
                elif len(B_charge) > 1:
                    answer += B_charge[1][0]
                elif len(A_charge) > 1:
                    answer += A_charge[1][0]

            # B에 더 큰 충전기가 있다면, 충전
            elif first in B_charge:
                B_charge.remove(first)
                if B_charge:
                    answer += B_charge[0][0]

            # 모두 아니라면, B 가장 큰 충전기로 충전
            elif B_charge:
                answer += B_charge[0][0]

        # A는 없고 B만 있다면, B만 충전
        elif B_charge:
            answer += B_charge[0][0]

        # N만큼 걸으면 이동 멈추기
        if m == N:
            break

        # A, B 이동
        A[0] += move[A_move[m]][0]
        A[1] += move[A_move[m]][1]
        B[0] += move[B_move[m]][0]
        B[1] += move[B_move[m]][1]

    print(f'#{tc} {answer}')

