# 16진수를 4자리의 2진수로 변환하는 함수
def fromHexaToBin(char):
    nums = list(map(str, range(10)))
    if char in nums:  # 숫자면 숫자 그대로
        num = int(char)
    else:  # 문자면 해당 문자에 맞게 숫자로 변환
        num = ord(char) - 55
    num = fromDecToBin(num, '')  # int를 str로 반환 (2진수형태)

    for i in range(3):  # 2진수로 변환했을 때 4자리보다 적으면, 4자리 맞추기
        if len(num) < 4:
            num = '0' + num

    return num


# 10진수를 2진수로 변환하는 함수
def fromDecToBin(n, result):
    if n == 0:
        return '0' + result
    elif n == 1:
        return '1' + result

    if n % 2:
        return fromDecToBin(n // 2, '1' + result)
    else:
        return fromDecToBin(n // 2, '0' + result)


################################################################################


testcase = int(input())

for tc in range(1, testcase+1):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]
    patterns = {'0001101': '0', '0011001': '1', '0010011': '2',
                '0111101': '3', '0100011': '4', '0110001': '5',
                '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

    text_list = []
    password_set = set()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '0':
                arr[i][j] = '0000'
            else:
                arr[i][j] = fromHexaToBin(arr[i][j])

    for i in range(N):
        row = ''
        for j in range(M):
            row += arr[i][j]

        acc = 0

        j = len(row) - 1
        while j >= 0:
            if row[j] != '0':
                break
            j -= 1

        for k in range(1, 90):
            length = 56 * k
            total_password = row[j-length+1 : j+1]
            if total_password[:k*7:k] in patterns:
                password = ''
                for m in range(8):
                    password += total_password[m*k*7:m*k*7+k*7:k]
                password_set.add(patterns[password])
                break

    print(password_set)

    # for password in password_set:
    #     acc = 0
    #     result = 0
    #     for i in range(len(password)):
    #         if i % 2:
    #             acc += int(patterns[password[i * 7:i * 7 + 7]])
    #         else:
    #             acc += int(patterns[password[i * 7:i * 7 + 7]]) * 3
    #         result += int(patterns[password[i * 7:i * 7 + 7]])


