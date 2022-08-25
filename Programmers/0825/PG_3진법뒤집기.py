def solution(n):
    def triad(n, result):
        if n // 3 == 0:
            return str(n % 3) + result

        return triad(n // 3, str(n % 3) + result)

    new = triad(n, '')[::-1]
    answer = 0

    for i in range(len(new)):
        answer += int(new[len(new) - i - 1]) * (3 ** i)

    return answer