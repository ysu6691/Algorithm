# 조합 만드는 함수
# 조합을 여러 번 사용할 것이기 때문에, 리스트 인자를 직접 넣어줘야 함
def comb(sample_list, blank_list, sidx, idx):
    if sidx == len(selection):
        blank_list.append(selection[:])
        return

    if idx == len(sample_list):
        return

    selection[sidx] = sample_list[idx]
    comb(sample_list, blank_list, sidx+1, idx+1)
    comb(sample_list, blank_list, sidx, idx+1)

testcase = int(input())
for tc in range(1, testcase+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

		# 각 재료의 인덱스를 저장한 리스트
		# 각 재료의 인덱스는 0 ~ N-1까지 존재
    positions = list(range(N))

    selection = [0] * (N//2)
    comb_list = []
    comb(positions, comb_list, 0, 0)
		# ex) N = 4
		# comb_list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

		# A음식에 [0, 1], B음식에 [2, 3]을 사용했다면,
    # A음식에 [2, 3], B음식에 [0, 1]을 사용할 필요가 없으므로, 조합 나누기
		# 조합 만드는 재귀함수의 특성에 의해,
    # comb_list를 반으로 나눈 뒤 둘 중 하나를 뒤집으면 서로 중복되지 않는 리스트 만들어짐
		# A_list = [[0, 1], [0, 2], [0, 3]]
		# B_list = [[2, 3], [1, 3], [1, 2]] -> A_list와 같은 인덱스일 때, 중복되는 값이 없다.
    A_list = comb_list[:len(comb_list)//2]
    B_list = comb_list[len(comb_list)-1:len(comb_list)//2-1:-1]

    min_gap = 987654321

		# 선택한 재료마다 해당 좌표값 더해 최솟값인지 확인
    for i in range(len(comb_list)//2):
				# A음식을 만드는 재료의 조합을 모두 고려 (조합 재사용)
				# ex) N = 6, i = 0
        # A_list = [[0, 1, 2], [0, 1, 3], [0, 1, 4], ..., [0, 4, 5]]
        # A_list[i] = [0, 1, 2]
        # A_positions = [[0, 1], [0, 2], [1, 2]]
        A = 0
        A_positions = []
        selection = [0] * 2
        comb(A_list[i], A_positions, 0, 0)

        for position in A_positions:
						# A에 해당 좌표 값 모두 더하기
            A += arr[position[0]][position[1]] + arr[position[1]][position[0]]

				# B도 동일하게 수행
        B = 0
        B_positions = []
        selection = [0] * 2
        comb(B_list[i], B_positions, 0, 0)
        for position in B_positions:
            B += arr[position[0]][position[1]] + arr[position[1]][position[0]]

        if abs(A - B) < min_gap:
            min_gap = abs(A - B)

    print(f'#{tc} {min_gap}')