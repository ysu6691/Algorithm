
# 1m^2당 참외의 개수 저장
N = int(input())

# field: 각 변의 길이 저장
# check: 각 방향이 몇 번 나왔는지 확인
# long: 두 개의 긴 변의 방향을 저장
field = []
check = []
long = []

for i in range(6):
    num, length = map(int, input().split())
    field.append([num, length])
    check.append(num)

for i in range(1, 5):
    if check.count(i) == 1:
        long.append(i)

# total_area: 긴 두 개의 변 저장
# del_idx: 빈 공간을 둘러싸는 두 개의 변을 제외한 나머지 인덱스를 저장 (i-1, i+1) 
total_area = []
del_idx = []


for i in range(6):
    if field[i][0] in long:
        total_area.append(field[i][1])
        if i - 1 < 0:                   # 만약 인접한 인덱스가 범위를 벗어나면,
            del_idx.append(i + 5)       # 반대편으로 이동
        else:
            del_idx.append(i - 1)
        if i + 1 > 5:
            del_idx.append(i - 5)
        else:
            del_idx.append(i + 1)

# empty: 빈 공간을 둘러싸는 두 변의 길이 저장
empty = []

for i in range(6):
    if i not in del_idx:
        empty.append(field[i][1])

# result = 구하고자 하는 면적
result = (total_area[0] * total_area[1]) - (empty[0] * empty[1])

print(result * N)