# an = ((n-1) * (an-1 + an-2))

N = int(input())

before_1 = 1
before_2 = 0
for num in range(3, N+1):
    answer = ((num - 1) * (before_1 + before_2)) % 1000000000
    before_1, before_2 = answer, before_1

if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    print(answer)