# queue 이용
testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # M번만큼 돌면서 앞에서 뒤로 보내기
    for _ in range(M):
        nums.append(nums.pop(0))

    # M번만큼 돌았을 때 가장 앞에 있는 값 출력
    print(f'#{tc} {nums[0]}')


# 나머지 이용
testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    print(f'#{tc} {nums[M%N]}')