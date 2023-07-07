def solution(money):
    
    dp = [[0, 0, 0, 0] for _ in range(len(money))]
    dp[0] = [money[0], 0, 0, 0]
    dp[1] = [0, money[1], money[1], 0]
    for i in range(1, len(money) - 1):
        dp[i][0] = dp[i - 1][1] + money[i]
        dp[i][1] = max(dp[i - 1][:2])
        dp[i][2] = dp[i - 1][3] + money[i]
        dp[i][3] = max(dp[i - 1][2:])
    dp[-1][:2] = dp[-2][:2]
    dp[-1][2] = dp[-2][3] + money[-1]
    dp[-1][3] = max(dp[-2][2:])
    
    return max(dp[-1])