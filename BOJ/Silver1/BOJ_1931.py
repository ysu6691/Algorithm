import sys, heapq
input = sys.stdin.readline

N = int(input())
time_list = []
for _ in range(N):
    start, end = map(int, input().split())
    time_list.append((start, end))

time_list.sort(key=lambda x: (x[1], x[0]))

answer = 0
before_end = 0
for time in time_list:
    if time[0] >= before_end:
        answer += 1
        before_end = time[1]

print(answer)

###########################

N = int(input())
queue = []
for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(queue, (end, start))

answer = 0
before_end = 0
while queue:
    end, start = heapq.heappop(queue)
    if start >= before_end:
        before_end = end
        answer += 1

print(answer)
