for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2): # 빌딩 하나씩 선택
        max_height = 0
        for j in [-2, -1, 1, 2]: # 좌우 두 채씩 확인
            if buildings[i] > buildings[i+j]: # 현재 빌딩이 더 높다면, 
                if buildings[i+j] > max_height: # 이웃 빌딩 중 가장 높은 빌딩 고르기 
                    max_height = buildings[i+j]
            else: # 더 높은 빌딩이 있다면,
                break # break
        else: # 현재 빌딩이 가장 높다면,
            result += buildings[i] - max_height # 결과 누적

    print(f'#{tc} {result}')
