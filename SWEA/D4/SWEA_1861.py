testcase = int(input())

for tc in range(1, testcase+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_list = [] # 이동거리가 최대일 때, 시작점을 저장할 리스트
    max_cnt = -1 # 최대 이동거리를 저장할 변수

    # NxN을 돌면서 이동
    for i in range(N):
        for j in range(N):
            start = [i, j]
            stack = [start]
            cnt = 1

            while stack:
                current = stack.pop()

                for k in range(4):
                    ni = current[0] + di[k]
                    nj = current[1] + dj[k]

                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] - arr[current[0]][current[1]] == 1:
                            stack.append([ni, nj])
                            # 이동할 수 있다면, cnt += 1
                            cnt += 1

            # 만약 현재 이동거리가 최대 이동거리보다 길다면,
            if cnt > max_cnt:
                max_cnt = cnt # 최대 이동거리 초기화
                max_list = [arr[i][j]] # 최대 이동거리일 때 시작점을 담는 리스트 초기화
            # 만약 현재 이동거리가 최대 이동거리라면,
            elif cnt == max_cnt:
                max_list.append(arr[i][j]) # 그때의 시작점 담기

    print(f'#{tc} {min(max_list)} {max_cnt}')