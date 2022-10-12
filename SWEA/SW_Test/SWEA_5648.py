from collections import defaultdict

testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    atom_dict = defaultdict(list)
    # 키를 현재 원자 위치로 하고, 이동 방향과 에너지를 리스트로 저장
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        atom_dict[(x, y)] = [(direction, energy)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    answer = 0
    finish = False

    # 시뮬레이션 시작
    while True:
        # 원자 위치와 방향, 에너지 받아오기
        for position, info in atom_dict.items():
            if info:
                direction, energy = info[0]
                # 지나치면서 합쳐지는 원자가 있는지 확인
                # 내가 이동할 방향에 원자가 있고, 이동방향이 반대라면 움직이면서 합쳐짐
                if direction == 0 and (position[0], position[1]+1) in atom_dict and atom_dict[(position[0], position[1]+1)]:
                    # 합쳐지는 원자가 있다면,
                    if atom_dict[(position[0], position[1]+1)][0][0] == 1:
                        answer += energy + atom_dict[(position[0], position[1]+1)][0][1] # 에너지 누적
                        atom_dict[(position[0], position[1])] = [] # 해당 리스트 빈 값으로
                        atom_dict[(position[0], position[1]+1)] = []
                if direction == 2 and (position[0]-1, position[1]) in atom_dict and atom_dict[(position[0]-1, position[1])]:
                    if atom_dict[(position[0]-1, position[1])][0][0] == 3:
                        answer += energy + atom_dict[(position[0]-1, position[1])][0][1]
                        atom_dict[(position[0], position[1])] = []
                        atom_dict[(position[0]-1, position[1])] = []

        # 이동했을 때 위치를 저장
        move_dict = defaultdict(list)
        for position, info in atom_dict.items():
            if info:
                info = info[0]
                nx = position[0] + dx[info[0]]
                ny = position[1] + dy[info[0]]
                # 만약 다른 원자와 더 이상 만날 수 없다면, 제거
                if -1000 <= nx < 1000 and -1000 <= ny < 1000:
                    move_dict[(nx, ny)].append((info[0], info[1]))

        # 다른 원자와 만났는지 확인
        for position, info in move_dict.items():
            # 만약 만났다면,
            if len(info) > 1:
                for i in range(len(info)-1, -1, -1):
                    answer += info[i][1] # 에너지 누적
                    move_dict[position].pop() # 제거

        # 현재 살아있는 원자만 다시 atom_list에 받아오기
        atom_dict = defaultdict(list)
        for position, info in move_dict.items():
            if info:
                atom_dict[position] = info

        # 더이상 남은 원자가 없다면, 종료
        if not atom_dict:
            finish = True
        else:
            for i in atom_dict.values():
                if i:
                    break
            else:
                finish = True
        if finish:
            break

    print(f'#{tc} {answer}')
