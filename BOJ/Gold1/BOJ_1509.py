import sys
input = sys.stdin.readline

string = input().strip()
size = len(string)

start_dict = dict()
for i in range(size):
    start_dict[i] = []
    gap = 0
    while i - gap >= 0 and i + gap < size:
        if string[i + gap] == string[i - gap]:
            start_dict[i - gap].append(i + gap)
        else:
            break
        gap += 1

    gap = 0
    while i - gap >= 0 and i + gap + 1 < size:
        if string[i - gap] == string[i + gap + 1]:
            start_dict[i - gap].append(i + gap + 1)
        else:
            break
        gap += 1
    
stack = [(0, 0)]
memo = [987654321] * (size + 1)
while stack:
    idx, cnt = stack.pop()
    if memo[idx] <= cnt:
        continue
    memo[idx] = cnt

    if idx == size:
        continue

    for next in start_dict[idx]:
        if cnt + 1 < memo[next + 1]:
            stack.append((next + 1, cnt + 1))

print(memo[-1])