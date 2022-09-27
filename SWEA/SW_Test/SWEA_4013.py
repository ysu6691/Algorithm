# 자기 자신과 옆 자석을 회전시키는 함수
def rotate(num, direction): # 현재 자석 번호와 회전 방향 받기
    # 존재하지 않는 자석이거나 이미 확인한 자석이라면, return
    if num < 1 or num > 4 or num in visited:
        return

    # 반시계방향이라면,
    if direction == -1:
        visited.append(num) # 일단 확인했다고 기록
        if arr[num][2] != arr[num+1][6]: # 오른쪽 자석 확인
            rotate(num+1, 1) # 맞닿아 있는 부분이 다르면, 시계방향으로 돌리기
        if arr[num][6] != arr[num-1][2]: # 왼쪽 자석 확인
            rotate(num-1, 1) # 맞닿아 있는 부분이 다르면, 반시계방향으로 돌리기
        arr[num].append(arr[num].pop(0)) # 자기 자신도 돌리기

    # 시계방향인 경우도 마찬가지로 진행
    if direction == 1:
        visited.append(num)
        if arr[num][2] != arr[num+1][6]:
            rotate(num+1, -1)
        if arr[num][6] != arr[num-1][2]:
            rotate(num-1, -1)
        arr[num].insert(0, arr[num].pop())

################################################################

testcase = int(input())

for tc in range(1, testcase+1):
    K = int(input())
    # 인덱스 오류를 피하기 위해 감싸기
    arr = [[0]*8]
    arr += [list(map(int, input().split())) for _ in range(4)] + [[0]*8]

    # K번만큼 실행
    for _ in range(K):
        num, direction = map(int, input().split())
        visited = []
        rotate(num, direction)

    # 맨 위 값에 따라 누적
    answer = 0
    for i in range(4):
        answer += arr[i+1][0] * 2**i

    print(f'#{tc} {answer}')
