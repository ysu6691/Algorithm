def solution(arrayA, arrayB):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # 최대공약수 구하기
    def fing_gcd_num(array):
        if len(array) == 1:
            return array[0]

        current_gcd = gcd(array[0], array[1])
        for num in array[2:]:
            current_gcd = gcd(current_gcd, num)
        return current_gcd

    # 최대공약수 반환
    gcd_A = fing_gcd_num(arrayA)
    gcd_B = fing_gcd_num(arrayB)

    # 최대공약수가 상대 그룹에서 나눠지는지 확인
    for num in arrayB:
        if not (num % gcd_A):
            gcd_A = 0
            break

    for num in arrayA:
        if not (num % gcd_B):
            gcd_B = 0
            break

    # 둘 중 더 큰 값 리턴
    answer = max(gcd_A, gcd_B)

    return answer
