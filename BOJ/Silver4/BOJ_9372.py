# 최소 비행기의 '종류'이므로 나라 - 1

testcase = int(input())

for tc in range(testcase):

    N, M = map(int, input().split())
    for _ in range(M):
        input() # 버리기

    print(N-1)