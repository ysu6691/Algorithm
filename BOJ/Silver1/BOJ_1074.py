import sys
input = sys.stdin.readline

def find_answer(r, c, power, cnt):

    if power == 1:
        for i in range(2):
            for j in range(2):
                if r + i == R and c + j == C:
                    return cnt
                cnt += 1

    if R < r + 2 ** (power - 1):
        if C < c + 2 ** (power - 1):
            return find_answer(r, c, power - 1, cnt)
        else:
            return find_answer(r, c + 2 ** (power - 1), power - 1, cnt + 2 ** (power * 2 - 2))
    else:
        if C < c + 2 ** (power - 1):
            return find_answer(r + 2 ** (power - 1), c, power - 1, cnt + 2 ** (power * 2 - 2) * 2)
        else:
            return find_answer(r + 2 ** (power - 1), c + 2 ** (power - 1), power - 1, cnt + 2 ** (power * 2 - 2) * 3)

N, R, C = map(int, input().split())

print(find_answer(0, 0, N, 0))
