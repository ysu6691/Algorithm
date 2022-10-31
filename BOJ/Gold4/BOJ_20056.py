from collections import defaultdict

N, M, K = map(int, input().split())
# key는 좌표, value는 (질량, 속도, 방향)
fireballs = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r, c)].append((m, s, d))

# 방향 순서대로 저장
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 시뮬레이션 시작
for _ in range(K):
    # 이동 후 좌표와 질량, 속도, 방향 정보를 새로운 defaultdict에 저장
    new_fireballs = defaultdict(list)
    for position in fireballs:
        r, c = position
        for fireball in fireballs[position]:
            m, s, d = fireball
            nr = r + dr[d] * s
            nc = c + dc[d] * s
            if not nr % N:
                nr = N
            else:
                nr %= N
            if not nc % N:
                nc = N
            else:
                nc %= N
            new_fireballs[(nr, nc)].append((m, s, d))

    # 이동 후 정보를 다시 원래 defaultdict에 넣기
    # 빈 상태에서 시작
    fireballs = defaultdict(list)
    for position in new_fireballs:
        # 좌표가 겹치는게 없다면 그냥 추가
        if len(new_fireballs[position]) == 1:
            fireballs[position].append(new_fireballs[position][0])
            continue

        # 좌표가 겹치면 합치기
        sum_m = 0
        sum_s = 0
        cnt = 0
        direction = new_fireballs[position][0][2] % 2
        is_same_direction = True
        for fireball in new_fireballs[position]:
            m, s, d = fireball
            sum_m += m
            sum_s += s
            cnt += 1
            # 방향이 다 짝수나 홀수가 맞는지 아닌지 확인
            if is_same_direction and d % 2 != direction:
                is_same_direction = False

        new_m = sum_m // 5
        if not new_m: # 질량이 0이면 추가x
            continue
        new_s = sum_s // cnt
        # 모두 홀수나 짝수면 다음 방향은 0, 2, 4, 8
        if is_same_direction:
            for i in range(0, 7, 2):
                fireballs[position].append((new_m, new_s, i))
        # 모두 홀수나 짝수가 아니면 다음 방향은 1, 3, 5, 7
        else:
            for i in range(1, 8, 2):
                fireballs[position].append((new_m, new_s, i))

answer = 0
for position in fireballs:
    for fireball in fireballs[position]:
        answer += fireball[0]

print(answer)