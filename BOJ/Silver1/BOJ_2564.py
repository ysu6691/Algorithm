width, height = map(int, input().split())

N = int(input())

stores =[list(map(int, input().split())) for _ in range(N)]

position = list(map(int, input().split()))

acc = 0

for store in stores:
    if position[0] == 1:
        if store[0] == 1:
            acc += abs(position[1] - store[1])
        elif store[0] == 2:
            if position[1] + store[1] < 2 * width - (position[1] + store[1]):
                acc += position[1] + store[1] + height
            else:
                acc += 2 * width - (position[1] + store[1]) + height
        elif store[0] == 3:
            acc += position[1] + store[1]
        elif store[0] == 4:
            acc += width - position[1] + store[1]

    if position[0] == 2:
        if store[0] == 1:
            if position[1] + store[1] < 2 * width - (position[1] + store[1]):
                acc += position[1] + store[1] + height
            else:
                acc += 2 * width - (position[1] + store[1]) + height
        elif store[0] == 2:
            acc += abs(position[1] - store[1])
        elif store[0] == 3:
            acc += position[1] + height - store[1]
        elif store[0] == 4:
            acc += width - position[1] + height - store[1]

    if position[0] == 3:
        if store[0] == 1:
            acc += position[1] + store[1]
        elif store[0] == 2:
            acc += height - position[1] + store[1]
        elif store[0] == 3:
            acc += abs(position[1] - store[1])
        elif store[0] == 4:
            if position[1] + store[1] < 2 * height - (position[1] + store[1]):
                acc += position[1] + store[1] + width
            else:
                acc += 2 * height - (position[1] + store[1]) + width

    if position[0] == 4:
        if store[0] == 1:
            acc += position[1] + width - store[1]
        elif store[0] == 2:
            acc += height - position[1] + width - store[1]
        elif store[0] == 3:
            if position[1] + store[1] < 2 * height - (position[1] + store[1]):
                acc += position[1] + store[1] + width
            else:
                acc += 2 * height - (position[1] + store[1]) + width
        elif store[0] == 4:
            acc += abs(position[1] - store[1])

print(acc)

