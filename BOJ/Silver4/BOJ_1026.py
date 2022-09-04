# 서로 곱한 값을 모두 더한게 가장 작으려면,
# 가장 큰 값은 가장 작은 값과 곱해야 함

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 오름차순, B는 내림차순
A.sort()
B.sort(reverse=True)

acc = 0

# 각 자리 곱해서 더하기
for i in range(N):
    acc += A[i] * B[i]

print(acc)
