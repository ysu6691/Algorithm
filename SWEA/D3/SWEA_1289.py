testcase = int(input())

for tc in range(1, testcase+1):

    bit = input()

    zero = True
    one = False
    cnt = 0

    for i in bit:
        if i == '1' and zero:
            one = True
            zero = False
            cnt += 1

        if i == '0' and one:
            cnt += 1
            one = False
            zero = True

    print(f'#{tc} {cnt}')

