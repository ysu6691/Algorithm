T = int(input())

for tc in range(1, T+1):
	N, M = map(int, input().split())

	numerator = 1
	denominator = 1

	for i in range(1, N+1):
		numerator *= i

	for i in range(M, M-N, -1):
		denominator *= i

	print(denominator // numerator)
