testcase = int(input())

for tc in range(1, testcase+1):

    input_list = list(input().split())

    nums = list(map(str, range(10)))

    stack = []

    for i in range(len(input_list)):
        if input_list[i][0] in nums:
            stack.append(int(input_list[i]))
        elif input_list[i] == '.':
            break
        else:
            if len(stack) >= 2:
                if input_list[i] == '+':
                    stack.append(stack.pop() + stack.pop())
                elif input_list[i] == '-':
                    stack.append(stack.pop(-2) - stack.pop())
                elif input_list[i] == '*':
                    stack.append(stack.pop() * stack.pop())
                elif input_list[i] == '/':
                    stack.append(stack.pop(-2) // stack.pop())
            else:
                stack = ['error']
                break

    if len(stack) > 1:
        stack = ['error']

    print(f'#{tc} {stack[0]}')
