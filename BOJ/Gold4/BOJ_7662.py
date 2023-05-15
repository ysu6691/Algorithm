import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    cnt = 0
    num_dict = dict()

    for _ in range(k):
        command, num = map(str, input().split())

        if command == "I":
            num = int(num)
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            cnt += 1
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        elif command == "D":
            if cnt == 0:
                continue

            if num == "1":
                while max_heap:
                    max_num = -heapq.heappop(max_heap)
                    if num_dict[max_num]:
                        num_dict[max_num] -= 1
                        break
            elif num == "-1":
                while min_heap:
                    min_num = heapq.heappop(min_heap)
                    if num_dict[min_num]:
                        num_dict[min_num] -= 1
                        break
            cnt -= 1

    if cnt == 0:
        print("EMPTY")
    else:
        while max_heap:
            max_num = -heapq.heappop(max_heap)
            if num_dict[max_num]:
                break
        while min_heap:
            min_num = heapq.heappop(min_heap)
            if num_dict[min_num]:
                break
        print(max_num, min_num)
