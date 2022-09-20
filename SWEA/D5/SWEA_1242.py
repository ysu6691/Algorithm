# 16진수를 4자리의 2진수로 변환하는 함수
def fromHexaToBin(char):
	nums = list(map(str, range(10)))
	if char in nums:  # 숫자면 숫자 그대로
		num = int(char)
	else:  # 문자면 해당 문자에 맞게 숫자로 변환
		num = ord(char) - 55
	num = fromDecToBin(num, '')  # int를 str로 반환 (2진수형태)

	for i in range(3):  # 2진수로 변환했을 때 4자리보다 적으면, 4자리 맞추기
		if len(num) < 4:
			num = '0' + num

	return num


# 10진수를 2진수로 변환하는 함수
def fromDecToBin(n, result):
	if n == 0:
		return '0' + result
	elif n == 1:
		return '1' + result

	if n % 2:
		return fromDecToBin(n // 2, '1' + result)
	else:
		return fromDecToBin(n // 2, '0' + result)


################################################################################


testcase = int(input())

for tc in range(1, testcase+1):
	N, M = map(int, input().split())

	arr = [list(input().strip()) for _ in range(N)]
	patterns = {'0001101': '0', '0011001': '1', '0010011': '2',
				'0111101': '3', '0100011': '4', '0110001': '5',
				'0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

	text_list = []
	password_set = set()

	# 16진수로 이루어진 2차원 배열을 모두 2진수로 변환
	for i in range(N):
		for j in range(M):
			if arr[i][j] == '0': # 0이면 함수 안 거치고 바로 '0000'으로 변환
				arr[i][j] = '0000'
			else:
				arr[i][j] = fromHexaToBin(arr[i][j])

	for i in range(N):
		# 한 행을 str로 가져오기
		row = ''
		for j in range(M):
			row += arr[i][j]

		acc = 0

		# 행의 끝에서부터 보면서, 1을 만나면 얼마만큼의 길이를 가진 암호인지 확인
		j = len(row) - 1
		while j >= 0:
			j -= 1
			if row[j] != '0':
				for k in range(1, 90):
					length = 56 * k
					total_password = row[j-length+1 : j+1] # 암호 길이 예상 (56, 112, 168, ...)
					check_password = total_password[-1:-7*k-1:-k] # 끝에서부터 한 자리 가져오기 (7, 14, 21, ...)
					next_k = False
					if check_password[::-1] in patterns: # 만약 예상한 암호 길이가 맞다면,
						password = ''
						for m in range(8):
							tmp_password = total_password[m*k*7:m*k*7+k*7:k] # 해당 비율에 맞춰서 암호 저장
							if tmp_password in patterns:
								password += (patterns[tmp_password])
							else: # 만약 가져온 길이가 우연히 맞은 거였다면,
								next_k = True # 다음 비율로 다시 검색
								break
						if next_k:
							continue
						password_set.add(password) # 암호 셋에 저장
						j -= length # 이어서 탐색
						break

	result = 0

	# 조건에 맞는 암호에 대해 누적해서 출력
	for password in password_set:
		check = 0
		acc = 0
		for i in range(8):
			if i % 2:
				acc += int(password[i])
				check += int(password[i])
			else:
				acc += int(password[i])
				check += int(password[i]) * 3
		if check % 10 == 0:
			result += acc

	print(f'#{tc} {result}')
