# 점화식 이용 (n = N//2)
# n이 홀수일 때, an = 2 * [a(n-1) + a1 * a(n-2) + a2 * a(n-3) + ... ] + a(n//2) * a(n//2)
# n이 짝수일 때, an = 2 * [a(n-1) + a1 * a(n-2) + a2 * a(n-3) + ... ]

N = int(input()) // 2
answer_list = [0, 1, 2]

for i in range(3, N+1):
    tmp = answer_list[i-1] * 2
    for j in range(1, i//2):
        tmp += 2 * answer_list[j] * answer_list[i - j - 1]
    if i % 2:
        tmp += answer_list[i//2] * answer_list[i//2]

    answer_list.append(tmp % 987654321)

print(answer_list[N])