N, K = map(int, input().split())

# 인덱스 맞추기 위해 0 넣고 시작
items_weight = [0]
items_value = [0]

for _ in range(N):
	W, V = map(int, input().split())

	# K보다 무거운 물건은 리스트에 담지 않기
	if W > K:
		continue

	items_weight.append(W)
	items_value.append(V)

# 리스트 길이 갱신
new_N = len(items_weight)

DP = [[0] * (K+1) for _ in range(new_N)]

# DP 2차원 배열의 열은 무게, 행은 각 물건의 인덱스
# 현재 행에 해당하는 물건의 가치와, 더 넣을 수 있는 만큼의 무게(열)를 이전 행에서 찾아서 더한다.
# 그 더한 값이 현재 열과 이전 행의 가치보다 크면, 값 갱신
for i in range(1, new_N):
	for j in range(1, K+1):
		if items_value[i] + DP[i-1][j - items_weight[i]] > DP[i-1][j] and j >= items_weight[i]:
			DP[i][j] = items_value[i] + DP[i-1][j - items_weight[i]]

		# 값을 갱신하지 못할 경우, 이전 행의 값을 그대로 가져오기
		else:
			DP[i][j] = DP[i-1][j]

print(DP[-1][-1])