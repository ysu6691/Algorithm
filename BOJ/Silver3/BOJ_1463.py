N = int(input())
DP = [[N]]
memo = set()
i = 0
result = 0
finish = False

while N > 1:
    DP.append([])

    for n in DP[i]:
        if not n % 3 and n // 3 not in memo:
            if n // 3 == 1:
                finish = True
                break
            DP[i+1].append(n//3)
            memo.add(n//3)
        if not n % 2 and n // 2 not in memo:
            if n // 2 == 1:
                finish = True
                break
            DP[i+1].append(n//2)
            memo.add(n//2)
        if n - 1 > 0 and n - 1 not in memo:
            DP[i+1].append(n-1)
            memo.add(n-1)

    i += 1

    if finish:
        result = i
        break

print(result)