import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocketmon_dict = dict()
pocketmon_list = [0]
for i in range(N):
    pocketmon = input().strip()
    pocketmon_dict[pocketmon] = i + 1
    pocketmon_list.append(pocketmon)

for _ in range(M):
    problem = input().strip()
    if problem.isdigit():
        print(pocketmon_list[int(problem)])
    else:
        print(pocketmon_dict[problem])