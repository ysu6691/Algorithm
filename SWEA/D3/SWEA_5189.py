def perm(depth, visited):
	# 만약 관리구역을 모두 방문했다면, 그 구역에서 다시 사무실로 돌아와야 함
	# 배터리 소비량이 최소면, 갱신
	if len(visited) == N:
		global min_sum
		selection[visited[-1]] = arr[visited[-1]][0]
		if sum(selection) < min_sum:
			min_sum = sum(selection)
		return

	# 현재 구역을 제외한 구역 중, 이미 방문하지 않은 구역 선택
	for i in range(N):
		if i != depth and i not in visited:
			selection[depth] = arr[depth][i]
			perm(i, visited+[i]) # 해당 구역으로 이동 (방문 기록 남기기)

testcase = int(input())

for tc in range(1, testcase+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]

	check = [0]*N
	selection = [0]*N
	min_sum = 1001
	perm(0, [0]) #  첫 번째 인자는 depth, 두 번째 인자는 visited

	print(f'#{tc} {min_sum}')