# 청소하기
def clean(r, c):
    # 일단 현재 위치 치우기
    arr[r][c] = 0

    # 현재 위치에서 오른쪽으로 가면서 쓰레기 있는지 확인
    for i in range(c+1, M):
        # 있으면 이동하기
        if arr[r][i]:
            clean(r, i)
            return # 현재 행에 있다면 다음 행은 보지 않기

    # 다음 행부터 보면서 쓰레기 있는지 확인
    for i in range(r+1, N):
        for j in range(c, M):
            # 있으면 이동하기
            if arr[i][j]:
                clean(i, j)
                return # 이미 이동했으므로 쓰레기 찾기 종료


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for r in range(N):
    for c in range(M):
        # 쓰레기 있으면 로봇 하나 생성하고 청소시키기
        if arr[r][c]:
            answer += 1
            clean(r, c)

print(answer)