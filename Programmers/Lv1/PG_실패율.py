def solution(N, stages):

    stage_list = [i for i in range(1, N+1)]
    stage_list.insert(0, 0)
    stage_list.append(0)
    success = [0] * (N+2)
    fail = [0] * (N+2)
    percentage = [0] * (N+2)

    for i in stages:
        for j in range(i):
            success[j+1] += 1
        fail[i] += 1

    for i in range(1, N+1):
        if success[i] == 0:
            percentage[i] = 0
        else:
            percentage[i] = fail[i] / success[i]

    for i in range(N, 1, -1):
        for j in range(1, i):
            if percentage[j] < percentage[j+1]:
                percentage[j], percentage[j+1] = percentage[j+1], percentage[j]
                stage_list[j], stage_list[j+1] = stage_list[j+1], stage_list[j]

    answer = stage_list[1:-1]

    return answer