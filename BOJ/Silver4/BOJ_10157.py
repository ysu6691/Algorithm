# 아이디어

# 가로 세로 길이 저장
C, R = map(int, input().split())

# 대기 순서 저장
N = int(input())

# 대기 순서가 총 면적보다 크면, 0 출력
if N > C * R:
    print(0)

# (1,1) ~ (C,R)의 가상의 좌표를 돌면서 대기 순서를 지나쳤는지 확인
# 지나쳤다면, 지나친만큼 좌표 수정
else:
    current = [1, 0]

    # 상, 우, 하, 좌 순서로 좌표 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n = 0
    finish = False

    while finish == False:

        for i in range(4):

            if dx[i]:
                current[0] += dx[i] * (C - 1)
                n += C - 1
                C -= 1
                if n >= N:
                    print(current[0] - (n - N) * dx[i], current[1])
                    finish = True # 찾았다면 while문 파괴
                    break

            elif dy[i]:
                current[1] += dy[i] * R
                n += R
                R -= 1
                if n >= N:
                    print(current[0], current[1] - (n - N) * dy[i])
                    finish = True
                    break