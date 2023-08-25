def solution(arr):
    
    def calculate(operation, num1, num2):
        if operation == "+":
            return num1 + num2
        return num1 - num2
    
    
    nums = list(map(int, arr[0: len(arr): 2]))
    operations = arr[1: len(arr) - 1: 2]
    N = len(nums)
    dp = [[[0, 0] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = [nums[i], nums[i]]
    
    for size in range(1, N):
        for start in range(N - 1):
            end = start + size
            if end >= N:
                continue
            max_num = -987654321
            min_num = 987654321
            for middle in range(start, end):
                for i in range(2):
                    for j in range(2):
                        max_num = max(max_num, calculate(operations[middle], dp[start][middle][i], dp[middle + 1][end][j]))
                        min_num = min(min_num, calculate(operations[middle], dp[start][middle][i], dp[middle + 1][end][j]))
            dp[start][end][0] = max_num
            dp[start][end][1] = min_num
    
    return dp[0][-1][0]