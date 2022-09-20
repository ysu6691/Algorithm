testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    patterns = {'0001101': '0', '0011001': '1', '0010011': '2',
                '0111101': '3', '0100011': '4', '0110001': '5',
                '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

    # 암호 찾기
    flag = False
    for i in range(N):
        for j in range(M-1, -1, -1):     # 모든 암호 패턴의 맨 뒤 숫자는 1이므로,
            if arr[i][j] == '1':         # 뒤에서 부터 탐색하면서 1이 있는지 확인
                code = arr[i][j-55:j+1]  # 1을 찾았다면, 56자리 암호 패턴 저장
                flag = True
                break
            if flag:
                break

    # code = 01110110110001011101101100010110001000110100100110111011
    acc = 0 # 암호가 유효한 코드인지 확인할 변수
    result = 0 # 찾은 암호 코드의 합계를 저장할 함수

    # 암호 코드 탐색
    for i in range(8):
        if i % 2:
            acc += int(patterns[code[i*7:i*7+7]]) # 짝수자리는 그대로 누적
        else:
            acc += int(patterns[code[i*7:i*7+7]]) * 3 # 홀수자리는 3곱해서 누적
        result += int(patterns[code[i*7:i*7+7]]) # 얘는 그냥 더하기

    # 만약 유효하지 않다면, 0 출력
    if acc % 10:
        result = 0

    print(f'#{tc} {result}')