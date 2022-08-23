for tc in range(1, 11):

    N = int(input())
    char = input()

    stack = []
    new_char = ''

    nums = list(map(str, range(10)))
    operators_inside = {'+': 1, '*': 2, '(': 0}
    operators_outside = {'+': 1, '*': 2, '(': 3}

    cnt = 0

    for i in range(N):
        if char[i] in nums:
            new_char += char[i]

        else:
            if not stack:
                stack.append(char[i])
                top = 0
            else:
                if char[i] == ')':
                    while top > -1:
                        if stack[top] == '(':
                            stack.pop()
                            top -= 1
                            break
                        new_char += stack.pop()
                        top -= 1

                else:
                    while top > -1 and operators_outside[char[i]] <= operators_inside[stack[top]]:
                        if stack[top] == '(':
                            stack.pop()
                            top -= 1
                            continue
                        new_char += stack.pop()
                        top -= 1

                    stack.append(char[i])
                    top += 1

    while stack:
        new_char += stack.pop()

    for i in range(len(new_char)):
        if new_char[i] in nums:
            stack.append(int(new_char[i]))
        else:
            if new_char[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif new_char[i] == '+':
                stack.append(stack.pop() + stack.pop())

    print(f'#{tc} {stack[0]}')

