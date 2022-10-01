import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))

for i in range(2, N+1):
    num_list[i] += num_list[i-1]

for i in range(M):
    start, end = map(int, input().split())
    print(num_list[end]-num_list[start-1])
