testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    
    # 이진탐색을 위한 변수 생성
    start = 0
    end = N//2
    result = -1 # 세제곱이 없으면 -1 출력

    # 이진탐색
    while start <= end:
        middle = (start + end) // 2

        if middle ** 3 > N:
            end = middle - 1
        elif middle ** 3 < N:
            start = middle + 1
        elif middle ** 3 == N:
            result = middle
            break

        # N이 1인 경우만 따로 예외 처리
        if N == 1:
            result = 1
            break

    print(f'#{tc} {result}')