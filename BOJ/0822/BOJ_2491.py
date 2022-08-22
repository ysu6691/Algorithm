N = int(input())

num_list = list(map(int, input().split()))

max_cnt = -1

i = 0
cnt = 1

while i < N - 1:
    if num_list[i] > num_list[i + 1]:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0
    i += 1
    cnt += 1

if cnt > max_cnt:
    max_cnt = cnt

i = 0
cnt = 1

while i < N - 1:
    if num_list[i] < num_list[i + 1]:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0

    i += 1
    cnt += 1

if cnt > max_cnt:
    max_cnt = cnt

print(max_cnt)
