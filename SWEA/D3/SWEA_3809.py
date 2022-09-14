testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())

    nums = ''

    while len(nums) < N:
        num_list = list(map(int, input().split()))

        while num_list:
            nums += str(num_list.pop(0))

    num = 0

    while True:
        if str(num) in nums:
            num += 1
        else:
            break

    print(f'#{tc} {num}')