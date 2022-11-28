from collections import defaultdict
from copy import deepcopy

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

answer = 0

while True:
    # 현재 2차원 배열의 행과 열 길이 저장
    len_r = len(arr)
    len_c = len(arr[0])

    # 확인하려는 좌표가 현재 행렬의 내부에 있을 때만 검사
    if r <= len_r and c <= len_c:
        if arr[r-1][c-1] == k:
            break

    # 답은 100일때까지만 검사
    answer += 1
    if answer == 101:
        answer = -1
        break

    new_arr = []

    # 행의 개수가 더 많은 경우
    if len_r >= len_c:
        max_length = len_c
        for i in range(len_r):
            # key: 등장한 숫자, value: 등장 횟수
            num_dict = defaultdict(int)
            # 행 하나씩 보기
            for j in range(len_c):
                if arr[i][j]:
                    num_dict[arr[i][j]] += 1
            # 등장 횟수, 등장한 숫자 순으로 오름차순 정렬
            # ex) num_dict = {1: 3, 2: 1}
            #     sorted_nums: [(2, 1), (1, 3)]
            #     tmp_list = [2, 1, 1, 3]
            sorted_nums = sorted(num_dict.items(), key=lambda item: (item[1], item[0]))
            tmp_list = []
            cnt = 0
            for num in sorted_nums:
                tmp_list.append(num[0]) # 등장한 숫자
                tmp_list.append(num[1]) # 등장 횟수
                cnt += 1
                # 행의 크기가 100이 되면 break
                if cnt == 50:
                    break
            # 현재 행의 크기가 최대면 해당 열의 크기 저장
            if len(tmp_list) > max_length:
                max_length = len(tmp_list)

            # 새로 구한 행을 모두 저장
            new_arr.append(tmp_list)

        # 최대 행의 크기보다 작은 행은 0으로 채우기
        for i in range(len_r):
            if len(new_arr[i]) < max_length:
                for j in range(max_length - len(new_arr[i])):
                    new_arr[i].append(0)
        arr = deepcopy(new_arr)

    # 열의 개수가 더 많은 큰 경우도 마찬가지로 적용
    elif len_r < len_c:
        max_length = len_r
        for i in range(len_c):
            num_dict = defaultdict(int)
            for j in range(len_r):
                if arr[j][i]:
                    num_dict[arr[j][i]] += 1
            sorted_nums = sorted(num_dict.items(), key=lambda item: (item[1], item[0]))
            tmp_list = []
            cnt = 0
            for num in sorted_nums:
                tmp_list.append(num[0])
                tmp_list.append(num[1])
                cnt += 1
                if cnt == 50:
                    break
                if len(tmp_list) > max_length:
                    max_length = len(tmp_list)
            new_arr.append(tmp_list)

        # 여기서는 전치해서 넣기
        tmp_arr = [[0] * len_c for _ in range(max_length)]
        for i in range(len_c):
            for j in range(max_length):
                if j >= len(new_arr[i]):
                    tmp_arr[j][i] = 0
                else:
                    tmp_arr[j][i] = new_arr[i][j]
        arr = deepcopy(tmp_arr)

print(answer)