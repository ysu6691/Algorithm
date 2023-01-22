def solution(cap, n, deliveries, pickups):

    # deliveries_idx: 남은 deliveries 중 가장 마지막 인덱스
    # pickups_idx: 남은 pickups 중 가장 마지막 인덱스

    # 0이 아닌 가장 마지막 인덱스 찾기
    for deliveries_idx in range(n - 1, -1, -1):
        if deliveries[deliveries_idx]:
            break
    else:
        deliveries_idx = -1
    for pickups_idx in range(n - 1, -1, -1):
        if pickups[pickups_idx]:
            break
    else:
        pickups_idx = -1
    answer = 0

    # 그리디
    while deliveries_idx >= 0 or pickups_idx >= 0:
        # 둘 중 더 큰 인덱스만큼 더하기
        answer += (max(deliveries_idx, pickups_idx) + 1) * 2

        # 택배 배달부터
        current_boxes = 0
        flag = False
        while deliveries_idx >= 0:
            # 0이 아닌 인덱스 찾기
            while not deliveries[deliveries_idx]:
                deliveries_idx -= 1
                if deliveries_idx == -1:
                    flag = True
                    break
            # 배달 다 했거나 최대만큼 했으면 break
            if flag or current_boxes == cap:
                break
            tmp = current_boxes # 기존 상자 수
            current_boxes = min(cap, current_boxes + deliveries[deliveries_idx]) # 배달할 수 있는만큼 배달하기
            deliveries[deliveries_idx] -= current_boxes - tmp # 해당 인덱스에 배달한 만큼 빼기

        # 빈 상자 수거도 마찬가지
        current_boxes = 0
        flag = False
        while pickups_idx >= 0:
            while not pickups[pickups_idx]:
                pickups_idx -= 1
                if pickups_idx == -1:
                    flag = True
                    break
            if flag or current_boxes == cap:
                break
            tmp = current_boxes
            current_boxes = min(cap, current_boxes + pickups[pickups_idx])
            pickups[pickups_idx] -= current_boxes - tmp

        # 배달 다 했으면 종료
        if deliveries_idx == -1 and pickups_idx == -1:
            break

    return answer
