import sys
from collections import deque
length, width, height = map(int, input().split())

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]

matrix = [[list(map(int, sys.stdin.readline().split())) for y in range(width)] for z in range(height)]

Q = deque()
for z in range(height):
    for y in range(width):
        for x in range(length):
            if matrix[z][y][x] == 1:
                Q.append((z, y, x))

while Q:
    z, y, x = Q.popleft()

    for dir in range(6):
        tempz = z + dz[dir]
        tempy = y + dy[dir]
        tempx = x + dx[dir]
        if 0 <= tempx < length and 0 <= tempy < width and 0 <= tempz < height and not matrix[tempz][tempy][tempx]:
            Q.append((tempz, tempy, tempx))
            matrix[tempz][tempy][tempx] = matrix[z][y][x] + 1

max_num = 0
flag = False
for z in range(height):
    for y in range(width):
        for x in range(length):
            if matrix[z][y][x] > max_num:
                max_num = matrix[z][y][x]
            elif matrix[z][y][x] == 0:
                max_num = 0
                flag = True
                break
        if flag:
            break
    if flag:
        break

print(max_num - 1)