N = int(input())

column_list = []

max_height = 0

for i in range(N):
    position, height = map(int, input().split())
    column_list.append([position, height])

    if height > max_height:
        max_height = height

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if column_list[j][0] < column_list[min_idx][0]:
            min_idx = j

    column_list[i], column_list[min_idx] = column_list[min_idx], column_list[i]

total_area = 0
i = 0
j = 0

while N != 1:

    j += 1

    if column_list[i][1] < column_list[j][1]:
        total_area += (column_list[j][0] - column_list[i][0]) * column_list[i][1]
        i = j

    if column_list[i][1] == max_height:
        break

p = N - 1
q = N - 1

while N != 1:

    q -= 1

    if column_list[p][1] < column_list[q][1]:
        total_area += (column_list[p][0] - column_list[q][0]) * column_list[p][1]
        p = q

    if column_list[p][1] == max_height:
        break

if N == 1:
    total_area = column_list[0][1]
else:
    total_area += max_height * (column_list[p][0] - column_list[i][0] + 1)

print(total_area)