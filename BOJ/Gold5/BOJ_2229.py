# 각 인덱스마다 두 가지 리스트를 저장한다.
# start_list: 현재 인덱스가 새로운 그룹의 시작인 경우
# end_list: 현재 인덱스가 이전 그룹의 마지막인 경우
# [현재까지 모든 누적 값, 현재 그룹 최댓값, 현재 그룹 최솟값]

N = int(input())
N_list = list(map(int, input().split()))
start_list = [[] for _ in range(N)]
end_list = [[] for _ in range(N)]

# 두 리스트 모두 첫 번째 숫자를 가지고 시작(누적값은 0)
# ex) 첫 번째 숫자: 2
#     start_list = [0, 2, 2]
#     end_list = [0, 2, 2]
start_list[0], end_list[0] = [0, N_list[0], N_list[0]], [0, N_list[0], N_list[0]]

for idx in range(1, N):
    # 현재 인덱스가 새로운 그룹의 시작이면 다음과 같이 정해진다.
    # [지금까지의 누적값, 현재 그룹 최댓값, 현재 그룹 최솟값]: [전까지의 누적값, 현재 인덱스 숫자, 현재 인덱스 숫자]
    start_list[idx] = [end_list[idx - 1][0], N_list[idx], N_list[idx]]

    # 현재 인덱스가 이전 그룹의 마지막이면 조건에 따라 분기한다.
    # 우선 이전 그룹 리스트 그대로 가져오기
    end_list[idx] = end_list[idx - 1]

    # 바로 이전 인덱스가 그룹의 시작인 경우부터 고려
    # 현재 숫자가 그룹의 최댓값인 경우
    if N_list[idx] > start_list[idx - 1][1]:
        # 현재까지 누적 값 + (현재 숫자 - 그룹의 최댓값이였던 것) > 그룹의 누적값이였던 것 이면,
        if start_list[idx - 1][0] + N_list[idx] - start_list[idx - 1][1] > end_list[idx][0]:
            # [새로운 누적 값, 현재 숫자(최댓값), 현재 그룹 최솟값(변화 x)]으로 변경
            end_list[idx] = [start_list[idx - 1][0] + N_list[idx] - start_list[idx - 1][1], N_list[idx], start_list[idx - 1][2]]
    # 현재 숫자가 그룹의 최솟값인 경우
    elif N_list[idx] < start_list[idx - 1][2]:
        # 현재까지 누적 값 + (그룹의 최솟값이였던 것 - 현재 숫자) > 그룹의 누적값이였던 것 이면,
        if start_list[idx - 1][0] + start_list[idx - 1][2] - N_list[idx] > end_list[idx][0]:
            # [새로운 누적 값, 현재 그룹 최솟값(변화 x), 현재 숫자(최솟값)]으로 변경
            end_list[idx] = [start_list[idx - 1][0] + start_list[idx - 1][2] - N_list[idx], start_list[idx - 1][1], N_list[idx]]

    # 바로 이전 인덱스가 그룹의 끝이였던 경우도 똑같이 고려
    # 현재 숫자가 그룹의 끝일 때 누적 값이 더 큰지 확인
    if N_list[idx] > end_list[idx - 1][1]:
        if end_list[idx - 1][0] + N_list[idx] - end_list[idx - 1][1] > end_list[idx][0]:
            end_list[idx] = [end_list[idx - 1][0] + N_list[idx] - end_list[idx - 1][1], N_list[idx], end_list[idx - 1][2]]
    elif N_list[idx] < end_list[idx - 1][2]:
        if end_list[idx - 1][0] + end_list[idx - 1][2] - N_list[idx] > end_list[idx][0]:
            end_list[idx] = [end_list[idx - 1][0] + end_list[idx - 1][2] - N_list[idx], end_list[idx - 1][1], N_list[idx]]

print(max(start_list[-1][0], end_list[-1][0]))
