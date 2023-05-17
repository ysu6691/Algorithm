def fibonacci(n):
    global cnt_0, cnt_1

    if n in memo:
        return memo[n]
    
    fibo1 = fibonacci(n - 2)
    fibo2 = fibonacci(n - 1)

    memo[n] = (fibo1[0] + fibo2[0], fibo1[1] + fibo2[1], fibo1[2] + fibo2[2])
    
    return memo[n]
    
T = int(input())
memo = {0: (0, 1, 0), 1: (0, 0, 1)}
for _ in range(T):
    cnt_0, cnt_1 = fibonacci(int(input()))[1:]
    print(cnt_0, cnt_1)