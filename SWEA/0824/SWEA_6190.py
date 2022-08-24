testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    nums = list(map(int, input().split()))

    max_num = -1

    for i in range(N-1):
        for j in range(i+1, N):
            num = nums[i]*nums[j]

            for k in range(len(str(num)) - 1):
                if int(str(num)[k]) > int(str(num)[k+1]):
                    break
            else:
                if num > max_num:
                    max_num = num

    print(f'#{tc} {max_num}')