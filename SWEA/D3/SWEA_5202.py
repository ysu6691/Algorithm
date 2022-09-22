testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    time_list = []

    end = 25 # 가장 빨리 끝나는 시간을 저장할 변수

    # 시작과 종료 시간을 받아, 리스트에 추가
    for _ in range(N):
        s, e = map(int, input().split())
        time_list.append((s, e))
        if e < end: # 가장 빨리 끝나는 시간 갱신
            end = e

    cnt = 1 # 이동한 화물차 수

    while end < 25:
        tmp_list = [] # 현재 작업보다 늦게 시작하는 작업만 담을 리스트
        tmp_end = 25 # 다음 작업시간 후보 중 가장 빨리 끝나는 시간

        for time in time_list:
            if time[0] >= end: # 만약 현재 작업보다 늦게 시작한다면,
                tmp_list.append(time) # 리스트에 추가
                if time[1] < tmp_end: # 만약 리스트에 추가된 후보 중 가장 빨리 끝난다면,
                    tmp_end = time[1] # 그 시간 갱신

        end = tmp_end
        if end == 25: # 가능한 다음 작업이 없다면 갱신되지 않았을 것이므로,
            break     # break

        cnt += 1
        time_list = tmp_list[:] # 다음 후보들로 리스트 갱신

    print(f'#{tc} {cnt}')