# 1 ~ N까지의 크기를 갖는 조합 구하기 (부분집합)
def comb(sidx, idx, n):
    if sidx == n:
        # 만약 고른 키가 B보다 크거나 같다면, 그 차이만큼 리스트에 추가
        if sum(selection) >= B:
            result.append(sum(selection) - B)
        return

    if idx == N:
        return

    selection[sidx] = height_list[idx]
    comb(sidx+1, idx+1, n)
    comb(sidx, idx+1, n)

testcase = int(input())

for tc in range(1, testcase+1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))
    result = []

    # 1 ~ N까지의 크기를 갖는 조합 구하기
    for i in range(1, N+1):
        selection = [0] * i
        comb(0, 0, i)

    # 조건에 맞는 값 중 최솟값 출력
    print(f'#{tc} {min(result)}')