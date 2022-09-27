# 다음 정류장으로 이동하는 함수
# cnt: 현재까지 충전 횟수, current: 현재 정류장 번호, battery: 현재 정류장 충전지
def move(cnt, current, battery):
    if current + battery >= N: # 만약 도착했다면,
        global min_cnt
        if cnt < min_cnt: # 최솟값 갱신
            min_cnt = cnt
        return

    # 도달할 수 있는 모든 정류장으로 이동해보기
    for i in range(current+1, current+battery+1):
        if cnt + 1 >= min_cnt: # 만약 최소 충전 횟수를 넘어갔다면,
            return # 백트래킹
        move(cnt+1, i, station_list[i])

testcase = int(input())

for tc in range(1, testcase+1):
    tmp = list(map(int, input().split()))
    N = tmp[0]
    station_list = tmp
    current = 1
    battery = station_list[1]
    min_cnt = 100

    move(0, 1, station_list[1])

    print(f'#{tc} {min_cnt}')