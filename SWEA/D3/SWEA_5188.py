testcase = int(input())

for tc in range(1, testcase+1):
	N = int(input())
	arr = [list(map(int, input().split())) for _ in range(N)]

	# 맨 위 행과 맨 왼쪽 열 누적해서 더하기
	for i in range(1, N):
		arr[0][i] += arr[0][i-1]
		arr[i][0] += arr[i-1][0]

	# 나머지 원소를 모두 확인하면서, 위와 왼쪽 원소 중 더 낮은 값 더하기
	for i in range(1, N):
		for j in range(1, N):
			arr[i][j] += min(arr[i-1][j], arr[i][j-1])

	# 맨 마지막 값 출력
	print(f'#{tc} {arr[-1][-1]}')