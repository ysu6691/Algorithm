# 16진수를 4자리의 2진수로 변환하는 함수
def fromHexaToBin(char):
    nums = list(map(str, range(10)))
    if char in nums: # 숫자면 숫자 그대로
        num = int(char)
    else: # 문자면 해당 문자에 맞게 숫자로 변환
        num = ord(char) - 55
    num = fromDecToBin(num, '') # int를 str로 반환 (2진수형태)

    for i in range(3): # 2진수로 변환했을 때 4자리보다 적으면, 4자리 맞추기
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

    N, text = input().split()
    answer = ''

    for char in text:
        answer += fromHexaToBin(char)

    print(f'#{tc} {answer}')
