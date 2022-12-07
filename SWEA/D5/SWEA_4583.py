testcase = int(input())
for tc in range(1, testcase+1):
    M, K = map(int, input().split())
    nums = list(range(7))
    change_list = []

    for i in range(M):
        idx1, idx2 = map(int, input().split())
        change_list.append((idx1-1, idx2-1))

    flag = False
    for cycle in range(1, K//M+1):
        for j in range(M):
            nums[change_list[j][0]], nums[change_list[j][1]] = nums[change_list[j][1]], nums[change_list[j][0]]
        if nums == [0, 1, 2, 3, 4, 5, 6]:
            flag = True
            break

    if flag:
        for i in range(K//M%cycle):
            for j in range(M):
                nums[change_list[j][0]], nums[change_list[j][1]] = nums[change_list[j][1]], nums[change_list[j][0]]
    for i in range(K % M):
        nums[change_list[i][0]], nums[change_list[i][1]] = nums[change_list[i][1]], nums[change_list[i][0]]


    answer = ''.join(map(str, nums))
    print(f'#{tc} {answer}')