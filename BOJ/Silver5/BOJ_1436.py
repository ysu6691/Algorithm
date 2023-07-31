N = int(input())

num = "1"
n = 0
while True:
    cnt = 0
    for i in range(len(num)):
        if num[i] == "6":
            cnt += 1
            if cnt == 3:
                n += 1
                break
        else:
            cnt = 0
    if n == N:
        break
    num = str(int(num) + 1)

print(num)