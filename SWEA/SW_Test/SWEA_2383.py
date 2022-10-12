from collections import defaultdict
from itertools import product
from copy import deepcopy

testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    position_dict = defaultdict(list)
    stair_list = []
    number = 0

    # 2차원 배열을 돌면서 현재 위치에 사람이 있으면, 사람 번호 매기고 가상 좌표 저장
    # 계단이 있으면, 계단 위치와 계단 길이 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                if arr[i][j] == 1:
                    position_dict[number] = [i, j]
                    number += 1
                else:
                    stair_list.append((i, j, arr[i][j]))

    # 중복순열로 사람 수 만큼 목표 계단 만들기
    product_list = []
    for i in product([0, 1], repeat=number):
        product_list.append(i)

    min_time = 987654321

    # 사람마다 목표 계단 하나씩 설정
    for destination in product_list:
        time = 0
        finish = False
        on_stairs = defaultdict(list)
        tmp_position_dict = deepcopy(position_dict)

        # 시뮬레이션 시작
        while True:
            move_list = []
            # 현재 사람과 위치 가져오기
            for number, position in tmp_position_dict.items():
                if position:
                    # 목표 계단 가져오기
                    current_destination = stair_list[destination[number]]
                    # 계단에서 떨어져 있다면, 계단으로 이동
                    if position[0] > current_destination[0]:
                        tmp_position_dict[number] = [position[0]-1, position[1]]
                    elif position[0] < current_destination[0]:
                        tmp_position_dict[number] = [position[0]+1, position[1]]
                    elif position[1] > current_destination[1]:
                        tmp_position_dict[number] = [position[0], position[1]-1]
                    elif position[1] < current_destination[1]:
                        tmp_position_dict[number] = [position[0], position[1]+1]
                    # 계단에 도착했다면,
                    else:
                        # 현재 계단에 들어갈 수 있는지 확인
                        if len(on_stairs[destination[number]]) < 3:
                            # 현재 계단에 사람이 3명보다 적다면 계단으로 들어가기
                            on_stairs[destination[number]].append(current_destination[2]+1)
                            tmp_position_dict[number] = [] # 내 원래 위치는 없애기
                        # 계단에 현재 사람이 3명 이상이라면,
                        else:
                            # 내가 밀고 내려갈 수 있는지 확인
                            can_insert = False
                            for i in range(len(on_stairs[destination[number]])):
								# 계단에 이동하기 1분 남은 사람이 있다면,
                                if on_stairs[destination[number]][i] == 1:
                                    can_insert = True # 밀고 들어갈 수 있음
                                    on_stairs[destination[number]][i] = 0 # 그 사람 밀기
                                    break
                            if can_insert:
                                on_stairs[destination[number]].append(current_destination[2] + 1)
                                tmp_position_dict[number] = []

            # 계단 안에 있는 사람들 확인
            for stairs in on_stairs.values():
                # 만약 계단에 사람이 있다면,
                if stairs:
                    # 내림차순 정렬 (시간이 가장 적게 남은 사람이 뒤로 가게)
                    stairs.sort(reverse=True)
                    # 뒤에서부터 돌면서 시간 1씩 깎기
                    for i in range(len(stairs)-1, -1, -1):
                        stairs[i] -= 1
                        if stairs[i] <= 0: # 0에 도달했다면,
                            stairs.pop() # 내보내기

            # 시간 1 추가
            time += 1
            # 백트래킹
            if time >= min_time:
                break

            # 남은 사람이 있는지 확인
            for stairs in on_stairs.values():
                if stairs:
                    break
            else:
                for position in tmp_position_dict.values():
                    if position:
                        break
                else:
                    finish = True
                    break

            if finish:
                break

        # 최소 시간 갱신
        if time < min_time:
            min_time = time

    print(f'#{tc} {min_time}')