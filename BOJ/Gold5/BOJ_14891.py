# 현재 상황에 따라 옆 톱니바퀴를 돌릴지 결정하는 함수
def rotate(n, d):
    # 이미 확인한 톱니바퀴는 check 하기
    check[n] = 1

    # 시계 방향으로 돈 경우
    if d == 1:
        if n - 1 > 0 and not check[n-1]:                  # 왼쪽 톱니바퀴가 존재하고 아직 확인하지 않았다면,
            if gears_list[n-1][2] != gears_list[n][6]:    # 맞닿아 있는 부분이 서로 다른지 확인
                rotate(n-1, -1)                           # 다르다면 왼쪽 톱니바퀴부터 다시 함수 실행
        if n + 1 < 5 and not check[n+1]:                  # 오른쪽 톱니바퀴도 동일하게 수행
            if gears_list[n+1][6] != gears_list[n][2]:
                rotate(n+1, -1)
        gears_list[n].insert(0, gears_list[n].pop()) # 현재 톱니바퀴는 옆 톱니바퀴에 상관없이 돌리기

    # 반시계 방향도 동일하게 수행
    else:
        if n - 1 > 0 and not check[n-1]:
            if gears_list[n-1][2] != gears_list[n][6]:
                rotate(n-1, 1)
        if n + 1 < 5 and not check[n+1]:
            if gears_list[n+1][6] != gears_list[n][2]:
                rotate(n+1, 1)
        gears_list[n].append(gears_list[n].pop(0))

# 톱니바퀴 현재 상태 저장
gears_list = [['0'] * 8] # 인덱스 맞추기
for i in range(4):
    gears_list.append(list(input()))

k = int(input())
for i in range(k):
    num, direction = map(int, input().split())
    check = [0] * 6 # 인덱스 오류 나지 않도록 길이 설정
    rotate(num, direction) # 톱니바퀴 돌릴 때마다 함수 실행

# 결과 출력
result = 0
if gears_list[1][0] == '1':
    result += 1
if gears_list[2][0] == '1':
    result += 2
if gears_list[3][0] == '1':
    result += 4
if gears_list[4][0] == '1':
    result += 8

print(result)