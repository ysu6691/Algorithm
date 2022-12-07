import sys
from collections import deque

L = int(input())
ML, MK = map(int, input().split())
C = int(input())
zombie_list = []
for i in range(L):
    hp = int(sys.stdin.readline())
    zombie_list.append(hp)

answer = 'YES'
mine_memo = deque() # 지뢰를 기억할 리스트

# 일단 사거리부터 보기
for idx in range(ML):
    # 사거리가가 더 짧을 수도 있음
    if idx == L:
        break
    # 기본 공격력이 좀비 체력보다 높으면 패스
    if zombie_list[idx] < MK:
        pass
    # 주어진 거리 내에 못 죽인다면 지뢰 쓰기
    elif zombie_list[idx] > (idx + 1 - len(mine_memo))*MK:
        if C == 0:
            answer = 'NO'
            break
        C -= 1
        # 이미 지뢰 있다면 맨 앞 지뢰 값을 고려해서 추가
        if mine_memo:
            mine_memo.append(ML-mine_memo[0])
        # 지뢰 없다면 사거리만큼의 값으로 추가
        else:
            mine_memo.append(ML)
    # 지뢰 있으면 맨 앞의 인덱스만 1 빼기
    if mine_memo:
        mine_memo[0] -= 1
        if mine_memo[0] == 0:
            mine_memo.popleft()

# 사거리 바깥도 마찬가지로 진행
if answer == 'YES':
    for i in range(ML, L):
        if zombie_list[i] < MK:
            continue
        elif zombie_list[i] > (ML - len(mine_memo)) * MK:
            if C == 0:
                answer = 'NO'
                break
            C -= 1
            if mine_memo:
                mine_memo.append(ML - mine_memo[0])
            else:
                mine_memo.append(ML)
        if mine_memo:
            mine_memo[0] -= 1
            if mine_memo[0] == 0:
                mine_memo.popleft()

print(answer)