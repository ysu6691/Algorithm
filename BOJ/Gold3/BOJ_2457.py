N = int(input())

flower_list = [list(map(int, input().split())) for _ in range(N)]
flower_list.sort(key=lambda x: (x[0], x[1]))

start_month = 3
start_day = 1
cnt = 0
finish = False

while True:

    new_list = []

    while True:

        if not flower_list:
            break

        if flower_list[0][0] == start_month and flower_list[0][1] > start_day:
            break
        elif flower_list[0][0] > start_month:
            break

        new_list.append(flower_list.pop(0))

    new_list.sort(key=lambda x: (x[2], x[3]))

    if new_list:
        flower = new_list[-1]

        if flower[2] == 12:
            cnt += 1
            break

    else:
        cnt = 0
        break

    start_month = flower[2]
    start_day = flower[3]

    cnt += 1

print(cnt)