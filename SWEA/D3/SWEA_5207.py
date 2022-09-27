# 이진탐색
def binarySearch(m, start, end, select):
    # 찾는 숫자가 없다면 False 반환
    if start > end:
        return False

    middle = (start + end) // 2

    # 찾았다면, True 반환
    if N_list[middle] == m:
        return True
    # 찾는 숫자가 현재 중간에 있는 숫자보다 작다면,
    elif N_list[middle] > m:
        if select == 'left': # 이전에 왼쪽 범위를 골랐는지 확인
            return False
        if binarySearch(m, start, middle-1, 'left'): # 왼쪽 범위로 들어가기
            return True
    # 찾는 숫자가 현재 중간에 있는 숫자보다 클 때도 마찬가지
    elif N_list[middle] < m:
        if select == 'right':
            return False
        if binarySearch(m, middle+1, end, 'right'):
            return True

testcase = int(input())

for tc in range(1, testcase+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list.sort()

    answer = 0

    for m in M_list:
        if binarySearch(m, 0, N-1, ''):
            answer += 1

    print(f'#{tc} {answer}')