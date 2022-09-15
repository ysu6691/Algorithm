testcase = int(input())

for tc in range(1, testcase+1):
    current = input()
    lose = 0

    for char in current:
        if char == 'x':
            lose += 1

    result = 'YES'
    if lose >= 8:
        result = 'NO'

    print(f'#{tc} {result}')