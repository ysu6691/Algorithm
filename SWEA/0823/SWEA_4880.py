def tournament(left, right):
    if left == right:
        return left

    elif right - left == 1:
        return battle(left, right)

    return battle(tournament(left, (left + right) // 2), tournament((left + right) // 2 + 1, right))


def battle(a, b):
    if cards[a] == 1:
        if cards[b] == 1 or cards[b] == 3:
            return a
        else:
            return b

    elif cards[a] == 2:
        if cards[b] == 2 or cards[b] == 1:
            return a
        else:
            return b

    elif cards[a] == 3:
        if cards[b] == 3 or cards[b] == 2:
            return a
        else:
            return b

testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    cards = list(map(int, input().split()))

    print(f'#{tc} {tournament(0, N-1)+1}')