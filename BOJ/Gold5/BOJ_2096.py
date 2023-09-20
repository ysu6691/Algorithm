import sys
input = sys.stdin.readline

N = int(input())
max_arr = [0, 0, 0]
min_arr = [0, 0, 0]

for _ in range(N):
    arr = list(map(int, input().split()))
    max_arr = [arr[0] + max(max_arr[:2]), arr[1] + max(max_arr), arr[2] + max(max_arr[1:])]
    min_arr = [arr[0] + min(min_arr[:2]), arr[1] + min(min_arr), arr[2] + min(min_arr[1:])]

print(max(max_arr))
print(min(min_arr))