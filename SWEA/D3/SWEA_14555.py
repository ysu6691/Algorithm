T = int(input())

for tc in range(1, T+1):
	text = input()

	cnt = 0

	for i in range(len(text)):
		if text[i] == '(':
			if i + 1 < len(text):
				if text[i+1] == ')' or text[i+1] == '|':
					cnt += 1
		elif text[i] == '|':
			if i + 1 < len(text) and text[i+1] == ')':
				cnt += 1

	print(f'#{tc} {cnt}')