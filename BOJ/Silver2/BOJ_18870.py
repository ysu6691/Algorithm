import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_set = set(num_list)
sorted_list = sorted(list(num_set))

num_dict = dict()
for i in range(len(sorted_list)):
    num_dict[sorted_list[i]] = i

answer = []
for num in num_list:
    answer.append(num_dict[num])

print(" ".join(map(str, answer)))
