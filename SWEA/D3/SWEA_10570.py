testcase = int(input())

for tc in range(1, testcase+1):

    A, B = map(int, input().split())

    cnt = 0

    for num in range(A, B+1):
        if str(num) == str(num)[::-1]:
            if int(num ** (1/2)) == num ** (1/2):
                if str(int(num ** (1/2))) == str(int(num ** (1/2)))[::-1]:
                    cnt += 1

    print(f'#{tc} {cnt}')