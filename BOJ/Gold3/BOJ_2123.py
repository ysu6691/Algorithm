T = int(input())
n = int(input())
list_a = list(map(int, input().split()))
m = int(input())
list_b = list(map(int, input().split()))

acc_a = [0] * (n + 1)
for i in range(n):
    acc_a[i + 1] = acc_a[i] + list_a[i]
acc_b = [0] * (m + 1)
for i in range(m):
    acc_b[i + 1] = acc_b[i] + list_b[i]

a_dict = dict()
for i in range(n):
    for j in range(i + 1, n + 1):
        gap = acc_a[j] - acc_a[i]
        if gap in a_dict:
            a_dict[gap] += 1
        else:
            a_dict[gap] = 1

answer = 0
for i in range(m):
    for j in range(i + 1, m + 1):
        gap = acc_b[j] - acc_b[i]
        target = T - gap
        if target in a_dict:
            answer += a_dict[target]

print(answer)