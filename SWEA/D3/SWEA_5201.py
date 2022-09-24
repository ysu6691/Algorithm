testcase = int(input())

for tc in range(1, testcase+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # 비교를 위한 정렬
    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    i = 0 # 트럭 인덱스
    j = 0 # 컨테이너 인덱스

    result = 0

    while i < M and j < N:
        if trucks[i] >= containers[j]: # 만약 가장 큰 트럭이 짐을 옮길 수 있다면,
            result += containers[j] # 옮기기
            i += 1 # 다음 트럭으로
            j += 1 # 다음 컨테이너로
        else: # 못 옮긴다면,
            j += 1 # 다음 컨테이너 확인 (트럭은 그대로)

    print(f'#{tc} {result}')
