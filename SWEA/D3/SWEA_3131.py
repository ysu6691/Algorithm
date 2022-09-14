num_list = [2]

for num in range(3, 1000000, 2):
    for n in range(3, int(num ** (1/2)) + 1, 2):
        if num % n == 0:
            break
    else:
        num_list.append(num)

print(' '.join(map(str, num_list)))
