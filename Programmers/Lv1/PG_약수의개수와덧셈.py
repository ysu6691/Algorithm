def solution(left, right):

    def factor(n):
        cnt = 0
        for i in range(1, n+1):
            if not n % i:
                cnt += 1

        if cnt % 2:
            return False
        else:
            return True

    answer = 0

    for i in range(left, right+1):
        if factor(i):
            answer += i
        else:
            answer -= i

    return answer