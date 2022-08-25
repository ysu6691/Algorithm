testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())

    # queue에서 대기하다가 화덕에 자리가 나면 넣어줌
    queue = list(map(int, input().split()))

    # 화덕 현황 리스트
    oven = []

    # 각 피자의 번호마다 완성이 됐는지 확인하는 리스트
    check = [0] * (M+1)

    # 피자 번호 붙이는 변수
    num = 0

    # 일단 화덕 채우기
    for i in range(N):
        oven.append([i+1, queue.pop(0)]) # 피자 번호와 치즈의 양을 함께 입력
        num += 1 # 화덕에 피자 넣을 때마다 피자 번호 붙이기

    # ex) oven = [[1, 7], [2, 2], [3, 6]]
 
    # 화덕에 피자가 한 개 남으면 while문 파괴
    finish = False

    while True:
        for i in range(N):
            # 화덕을 돌면서 각 치즈를 반으로 줄이기
            oven[i][1] //= 2

            # 만약 i번째 치즈가 다 녹았다면, check에 추가
            if oven[i][1] == 0:
                check[oven[i][0]] = 1

                # 큐에 피자가 대기하고 있다면, 빈 자리(i번째)에 화덕에 넣어주기
                if queue:
                    num += 1
                    oven[i][0] = num
                    oven[i][1] = queue.pop(0)

                # 만약 check에 M-1만큼 체크가 되었다면, break
                if sum(check) == M - 1:
                    finish = True
                    break

        if finish:
            break

    # 체크 되어있지 않은 피자 번호 출력
    for i in range(1, M+1):
        if not check[i]:
            print(f'#{tc} {i}')
            break