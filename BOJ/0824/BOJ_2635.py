def rule(before, after, cnt):

    if before < after:
        tmp_list.append(after)
        return cnt

    tmp_list.append(after)
    return rule(after, before - after, cnt+1)


N = int(input())

num = 0

max_cnt = 0

while N >= num:
    tmp_list = [N]

    tmp_cnt = rule(N, num, 2)

    if tmp_cnt > max_cnt:
        max_cnt = tmp_cnt
        result = tmp_list[:]

    num += 1

print(max_cnt)
print(' '.join(map(str, result)))