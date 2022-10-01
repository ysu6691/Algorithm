testcase = int(input())

for tc in range(1, testcase+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 일꾼 한 명 먼저 벌통 놓기
    for i in range(N):
        for j in range(N-M+1):
            visited = []
            for k in range(M):
                visited.append((i, j+k)) # 놓은 벌통 기억

            # 놓은 벌통에 해당하는 꿀 양 저장
            A_list = []
            for k in range(M):
                A_list.append(arr[i][j+k])

            # 부분집합 생성
            selection = []
            for p in range(1 << M):
                flag = False
                tmp = []
                for q in range(M):
                    if p & (1 << q):
                        tmp.append(A_list[q])
                        if sum(tmp) > C: # 만약 꿀의 양이 C를 넘는 부분집합이 나오면,
                            flag = True  # 저장x
                            break
                if flag:
                    continue
                selection.append(tmp)

            # 가능한 부분집합 중, 제곱의 합이 가장 큰 집합 골라서 저장
            max_A = 0
            for s in selection:
                tmp = 0
                for k in range(len(s)):
                    tmp += s[k] ** 2
                if tmp > max_A:
                    max_A = tmp

            # 나머지 일꾼도 똑같이 실행
            for p in range(N):
                for q in range(N-M+1):
                    flag = False
                    for k in range(M):
                        if (p, q+k) in visited: # 만약 이미 벌통을 놓은 곳이면,
                            flag = True         # 다음 좌표로
                            break
                    if flag:
                        continue

                    B_list = []
                    for k in range(M):
                        B_list.append(arr[p][q + k])

                    selection = []
                    for n in range(1 << M):
                        flag = False
                        tmp = []
                        for m in range(M):
                            if n & (1 << m):
                                tmp.append(B_list[m])
                                if sum(tmp) > C:
                                    flag = True
                                    break
                        if flag:
                            continue
                        selection.append(tmp)

                    max_B = 0
                    for s in selection:
                        tmp = 0
                        for k in range(len(s)):
                            tmp += s[k] ** 2
                        if tmp > max_B:
                            max_B = tmp

                    # 두 일꾼이 모은 꿀의 양이 최대면, 갱신
                    if max_A + max_B > answer:
                        answer = max_A + max_B

    print(f'#{tc} {answer}')