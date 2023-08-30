import sys
from math import comb
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
positive_nums = []
negative_nums = []
positive_dict = dict()
negative_dict = dict()
zero_cnt = 0

for num in nums:
    if num > 0:
        if num not in positive_dict:
            positive_nums.append(num)
        positive_dict[num] = 1 if num not in positive_dict else positive_dict[num] + 1
    elif num < 0:
        if num not in negative_dict:
            negative_nums.append(num)
        negative_dict[num] = 1 if num not in negative_dict else negative_dict[num] + 1
    else:
        zero_cnt += 1

positive_nums.sort()
negative_nums.sort(reverse=True)

answer = 0
for positive_num in positive_nums:
    for negative_num in negative_nums:
        if positive_num < -negative_num:
            if -(positive_num + negative_num) in positive_dict:
                if positive_num > -(positive_num + negative_num):
                    answer += negative_dict[negative_num] * positive_dict[-(positive_num + negative_num)] * positive_dict[positive_num]
                elif positive_num == -(positive_num + negative_num) and positive_dict[positive_num] > 1:
                    answer += comb(positive_dict[positive_num], 2) * negative_dict[negative_num]
        elif positive_num == -negative_num:
            answer += zero_cnt * positive_dict[positive_num] * negative_dict[negative_num]
        else:
            if -(positive_num + negative_num) in negative_dict:
                if negative_num > -(positive_num + negative_num):
                    answer += negative_dict[negative_num] * negative_dict[-(positive_num + negative_num)] * positive_dict[positive_num]
                elif negative_num == -(positive_num + negative_num) and negative_dict[negative_num] > 1:
                    answer += comb(negative_dict[negative_num], 2) * positive_dict[positive_num]

if zero_cnt > 2:
    answer += comb(zero_cnt, 3)

print(answer)
