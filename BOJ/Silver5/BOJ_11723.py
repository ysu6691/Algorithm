import sys

N = int(input())
num_set = set()

for i in range(N):
    command_input = sys.stdin.readline().rstrip()
    if command_input == 'all':
        num_set = set(range(1, 21))
    elif command_input == 'empty':
        num_set = set()
    else:
        command, num = map(str, command_input.split())
        num = int(num)
        if command == 'add':
            num_set.add(num)
        elif command == 'remove' and num in num_set:
            num_set.remove(num)
        elif command == 'check':
            if num in num_set:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)
