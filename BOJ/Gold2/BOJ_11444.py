import sys
input = sys.stdin.readline

def multiply_matrix(matrix1, matrix2):
    new_matrix = [[0, 0], [0, 0]]
    for r in range(2):
        for c in range(2):
            new_matrix[r][c] = (matrix1[r][0] * matrix2[0][c] + matrix1[r][1] * matrix2[1][c]) % 1000000007
    return new_matrix

n = int(input())
dp = [[[0] * 2 for _ in range(2)] for _ in range(61)]
dp[0][0][0] = 1
dp[1][0][0] = 1
dp[1][0][1] = 1
dp[1][1][0] = 1

for i in range(1, 60):
    dp[i + 1] = multiply_matrix(dp[i], dp[i])

power = 59
current_matrix = [[1, 0], [0, 1]]
while power >= 0:
    if n >= 1 << power:
        current_matrix = multiply_matrix(current_matrix, dp[power + 1])
        n -= 1 << power
    power -= 1
    
print(current_matrix[0][1])