def solution(land, P, Q):
    size = len(land)
    if size == 1:
        return 0
    nums = []
    num_dict = dict()
    for r in range(size):
        for c in range(size):
            if land[r][c] in num_dict:
                num_dict[land[r][c]] += 1
            else:
                nums.append(land[r][c])
                num_dict[land[r][c]] = 1
    nums.sort()
    
    N = len(nums)
    right_acc = [0] * N
    left_acc = [0] * N
    right_acc[0] = num_dict[nums[0]]
    left_acc[-1] = num_dict[nums[-1]]
    for i in range(1, N):
        left_acc[N - i - 1] = left_acc[N - i] + num_dict[nums[N - i - 1]]
        right_acc[i] = right_acc[i - 1] + num_dict[nums[i]]
        
    dp = []
    dp.append([0, 0])
    tmp = 0
    for i in range(1, N):
        num = nums[i]
        tmp += (num - nums[0]) * num_dict[num]
    dp[0][1] = tmp
    answer = tmp * Q
    
    min_idx = 0
    for i in range(1, N):
        tmp = [0, 0]
        tmp[0] = dp[i - 1][0] + right_acc[i - 1] * (nums[i] - nums[i - 1])
        if i < N - 1:
            tmp[1] = dp[i - 1][1] - (left_acc[i + 1] + num_dict[nums[i]]) * (nums[i] - nums[i - 1])
        if tmp[0] * P + tmp[1] * Q < answer:
            answer = tmp[0] * P + tmp[1] * Q
        dp.append(tmp)
    
    return answer