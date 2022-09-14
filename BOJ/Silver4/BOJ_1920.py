def binarysearch(n, start, end):

    while start <= end:
        middle = (start + end) // 2

        if N_list[middle] > n:
            end = middle - 1
        elif N_list[middle] < n:
            start = middle + 1
        else:
            return 1

    return 0

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

for m in M_list:
    print(binarysearch(m, 0, N-1))
