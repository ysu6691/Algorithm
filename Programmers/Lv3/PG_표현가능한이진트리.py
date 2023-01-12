# 아이디어
# 1. 자식 노드가 1이면 해당 노드의 모든 조상 노드는 무조건 1이어야 한다.
# 2. 이진수 변환 후 0을 채워 완전 이진 트리로 변환
#    ex) 20 -> 10100 -> 0010100
# 3. 부모 노드(가운데 인덱스)부터 자식 노드로 내려가면서 본인은 0이지만 자식이 1인 경우를 발견하면 0으로 저장하기

def solution(numbers):

    # 이진수로 변환
    def convert_to_binary(n):
        if n < 2:
            return str(n)
        if n % 2:
            return convert_to_binary(n // 2) + '1'
        else:
            return convert_to_binary(n // 2) + '0'

    # 이진트리로 표현 가능한지 확인
    # idx: 현재 노드, power: 현재 깊이, is_one: 부모 노드가 1이었는지
    def check(idx, power, is_one):
        nonlocal result

        # 리프노드까지 내려가면 종료
        if power == -2:
            return

        # 백트래킹
        if not result:
            return

        # 자식 노드가 0이면 다음 노드로 내려가기
        if binary[idx] == '0':
            check(idx - 2 ** power, power - 1, False)
            check(idx + 2 ** power, power - 1, False)
        # 부모 노드가 0이었는데 자식 노드가 1이면 0으로 저장
        elif binary[idx] == '1' and not is_one:
            result = 0
            return
        # 부모 노드가 1이었는데 자식 노드도 1이면 다음 노드로 내려가기
        elif binary[idx] == '1' and is_one:
            check(idx - 2 ** power, power - 1, True)
            check(idx + 2 ** power, power - 1, True)

    answer = []
    for number in numbers:
        result = 1
        # 이진수로 변환
        binary = convert_to_binary(number)
        # 나머지 0으로 채우기
        i = 0
        while True:
            if 2 ** (2 ** i - 1) <= number < 2 ** (2 ** (i + 1) - 1):
                binary = '0' * (2 ** (i + 1) - 1 - len(binary)) + binary
                break
            i += 1
        # 루트 노드가 0이면 볼 필요 x
        if binary[(2 ** (i + 1) - 1) // 2] == '0':
            result = 0
        check((2 ** (i + 1) - 1) // 2, i - 1, True)
        answer.append(result)

    return answer
