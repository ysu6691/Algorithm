testcase = int(input())

for tc in range(1, testcase+1):

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

	# 이후 백트래킹을 위해, 전체 집 개수 구하기
    total_home = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                total_home += 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    result = -1

    finish = False

    for i in range(N):
        for j in range(N):
			# 행렬의 한 좌표에서 영역을 늘리면서 탐색
			# 행렬 가운데에 있는 좌표는 그만큼 더 멀리 탐색해야 함
            for k in range(N - abs(N - (i+j))+2):
                queue = [(i, j, 1)]
                visited = set()
                cost = k*k + (k-1)*(k-1) # 비용
                gain = 0 # 수익
                home = 0 # 찾은 집 개수

                while queue:
                    current = queue.pop(0)
                    if (current[0], current[1]) not in visited:
                        visited.add((current[0], current[1]))
						# 집을 찾았을 경우
                        if arr[current[0]][current[1]] == 1:
                            home += 1 
                            gain += M

                        if current[2]+1 <= k:
                            for d in range(4):
                                ni = current[0] + di[d]
                                nj = current[1] + dj[d]

                                if 0 <= ni < N and 0 <= nj < N:
                                    if (ni, nj) not in visited:
                                        queue.append((ni, nj, current[2]+1))

				# 손해 없이 최대 집 개수를 찾았을 경우, 결과값 갱신
                if gain - cost >= 0 and home > result:
                    result = home
								
				# 찾은 집 개수가 최대 집 개수와 같다면, 더이상 찾을 필요 x
                if result == total_home:
                    finish = True
                    break
            if finish:
                break
        if finish:
            break

    print(f'#{tc} {result}')