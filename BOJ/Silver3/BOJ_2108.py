import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

acc = 0
cnt_dict = dict()
for num in num_list:
    acc += num
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

if acc == 0:
    avg = 0
else:
    if not int(acc / N) % 2 and (acc / N) % (acc / N) in (0.5, -0.5):
        avg = round(acc / N) + 1
    else:
        avg = round(acc / N)

max_cnt = -1
max_cnt_num = -1
candidate = []
for num in cnt_dict:
    if cnt_dict[num] > max_cnt:
        max_cnt = cnt_dict[num]
        max_cnt_num = num
        candidate = [num]
    elif cnt_dict[num] == max_cnt:
        max_cnt_num = num
        candidate.append(num)

if len(candidate) > 1:
    max_cnt_num = sorted(candidate)[1]

num_list.sort()

middle = num_list[N // 2]

if N == 1:
    gap = 0
else:
    gap = num_list[-1] - num_list[0]

print(avg)
print(middle)
print(max_cnt_num)
print(gap)