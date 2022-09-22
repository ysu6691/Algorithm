# 베이비진인지 확인하는 함수
def babygin(p):
    # triplet
    for i in range(10):
        if p[i] >= 3:
            return True
    # run
    for i in range(8):
        if p[i] and p[i+1] and p[i+2]:
            return True

testcase = int(input())

for tc in range(1, testcase+1):
    card_list = list(map(int, input().split()))

    player1 = [0] * 10 # 카운트 배열
    player2 = [0] * 10 # 카운트 배열
    result = 0

    # 카드 받을 때마다 베이비진인지 확인
    for i in range(len(card_list)):
        if not i % 2:
            player1[card_list[i]] += 1
            if babygin(player1):
                result = 1
                break
        else:
            player2[card_list[i]] += 1
            if babygin(player2):
                result = 2
                break

    print(f'#{tc} {result}')