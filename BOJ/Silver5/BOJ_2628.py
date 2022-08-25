# 아이디어
# 가로와 세로 모두 가장 긴 길이를 갖는 조각을 찾아야 함
# 가로와 세로 각각 자르는 구간 별로 길이를 구해, 가장 긴 길이 서로 곱하기

# 가로, 세로 저장
width, height = map(int, input().split())

# 자르는 횟수 저장
N = int(input())

width_list = []
height_list = []

# 가로와 세로 각각 자르는 지점 리스트에 추가 
for _ in range(N):

    check, number = map(int, input().split())

    if check == 1:
        width_list.append(number)
    elif check == 0:
        height_list.append(number)

# 총 길이도 리스트에 추가
width_list.append(width)
height_list.append(height)

# 오름차순 정렬
width_list.sort()
height_list.sort()

# 각 자르는 지점 별로 그 길이를 측정
# 가장 긴 길이를 갖는 구간 찾기
# 가로와 세로 모두 가장 긴 길이를 갖는 조각의 넓이가 가장 큼
max_gap_width = 0
start = 0

for end in width_list:
    gap = end - start
    if gap > max_gap_width:
        max_gap_width = gap
    start = end

max_gap_height = 0
start = 0

for end in height_list:
    gap = end - start
    if gap > max_gap_height:
        max_gap_height = gap
    start = end

print(max_gap_width * max_gap_height)

