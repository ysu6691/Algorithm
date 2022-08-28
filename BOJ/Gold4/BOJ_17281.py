def perm(depth):
    if depth == 8:
        idx = selection[:]
        idx.insert(3, 0)
        player_list.add(tuple(idx))
        return

    for i in range(8):
        if not check[i]:
            check[i] = 1
            selection[depth] = idx_list[i]
            perm(depth+1)
            check[i] = 0

check = [0] * 8
selection = [0] * 8
idx_list = list(range(1, 9))
player_list = set()

perm(0)

N = int(input())
score_list = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

for players in player_list:
    player_idx = 0
    score = 0

    for i in range(N):
        out = 0
        current = [0, 0, 0]

        while True:
            player_score = score_list[i][players[player_idx]]
            if player_score == 0:
                out += 1
                if out == 3:
                    player_idx += 1
                    if player_idx == 9:
                        player_idx = 0
                    break

            elif player_score == 1:
                if current[2]:
                    score += 1
                current[2] = current[1]
                current[1] = current[0]
                current[0] = 1

            elif player_score == 2:
                if current[2]:
                    score += 1
                if current[1]:
                    score += 1
                current[2] = current[0]
                current[1] = 1
                current[0] = 0

            elif player_score == 3:
                if current[2]:
                    score += 1
                if current[1]:
                    score += 1
                    current[1] = 0
                if current[0]:
                    score += 1
                    current[0] = 0
                current[2] = 1

            elif player_score == 4:
                if current[2]:
                    score += 1
                    current[2] = 0
                if current[1]:
                    score += 1
                    current[1] = 0
                if current[0]:
                    score += 1
                    current[0] = 0
                score += 1

            player_idx += 1
            if player_idx == 9:
                player_idx = 0
    if score > max_score:
        max_score = score

print(max_score)