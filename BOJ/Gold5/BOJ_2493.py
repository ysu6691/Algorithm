import sys, heapq
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

answer = [0] * (N)
idx_memo = [(heights[-1], N - 1)]
for i in range(N - 2, -1, -1):
    while idx_memo:
        if heights[i] > idx_memo[0][0]:
            height, idx = heapq.heappop(idx_memo)
            answer[idx] = i + 1
        else:
            break
    heapq.heappush(idx_memo, (heights[i], i))

print(" ".join(map(str, answer)))