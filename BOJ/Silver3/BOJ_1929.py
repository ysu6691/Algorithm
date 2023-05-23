M, N = map(int, input().split())

arr = [0] * 1000001
for i in range(2, 1000000):
    if arr[i] == 0:
        j = 2
        while i * j <= 1000000: 
            arr[i * j] = 1
            j += 1

for i in range(max(2, M), N + 1):
    if not arr[i]:
        print(i)