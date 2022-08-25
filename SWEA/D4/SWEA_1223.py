for tc in range(1, 11):

    N = int(input())
    char = input()

    stack = []
    new_char = ''

    nums = list(map(str, range(10)))
    operators = {'+': 1, '*': 2}

    for i in range(N):
        if char[i] in nums:
            new_char += char[i]

        else:
            if not stack:
                stack.append(char[i])
                top = 0
            else:
                while top > -1 and operators[char[i]] <= operators[stack[top]]:
                    new_char += stack.pop()
                    top -= 1

                stack.append(char[i])
                top += 1

    while stack:
        new_char += stack.pop()

    for i in range(N):
        if new_char[i] in nums:
            stack.append(int(new_char[i]))
        else:
            if new_char[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif new_char[i] == '+':
                stack.append(stack.pop() + stack.pop())

    print(f'#{tc} {stack[0]}')

