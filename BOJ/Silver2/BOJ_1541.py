import sys
input = sys.stdin.readline

problem = input().strip()
split_problem = problem.split("-")

if not split_problem[0]:
    answer = 0
else:
    answer = sum(map(int, split_problem[0].split("+")))

for i in split_problem[1:]:
    nums = map(int, i.split("+"))
    answer -= sum(nums)

print(answer)