def combination(sidx, idx):
    if sidx == 3:
        comb_list.append(selection[:])
        return

    if idx == 7:
        return

    selection[sidx] = num_list[idx]
    combination(sidx+1, idx+1)
    combination(sidx, idx+1)

testcase = int(input())

for tc in range(1, testcase+1):

    num_list = list(map(int, input().split()))
    selection = [0]*3
    comb_list = []
    combination(0, 0)

    sum_set = set()

    for comb in comb_list:
        sum_set.add(sum(comb))

    sum_list = sorted(list(sum_set))

    print(f'#{tc} {sum_list[-5]}')