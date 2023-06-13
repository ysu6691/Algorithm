import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    commands = input().strip()
    p = int(input())
    nums = list(map(lambda x: int(x) if x else 0, input().strip()[1:-1].split(",")))
    
    # 정방향: 1, 역방향: 2
    direction = 1
    idx = 0
    start = 0
    end = p - 1

    for command in commands:
        if command == "R":
            if direction == 1:
                idx = end
                direction = 2
            else:
                idx = start
                direction = 1

        else:
            if start > end or not nums[0]:
                print("error")
                break
            if direction == 1:
                idx += 1
                start += 1
            else:
                idx -= 1
                end -= 1

    else:
        if not nums[0]:
            print("[]")
        elif direction == 1:
            print(f"[{','.join(map(str, nums[start: end + 1]))}]")
        else:
            print(f"[{','.join(map(str, nums[end: start: -1] + [nums[start]]))}]")
