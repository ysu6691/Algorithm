N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

# 가장 큰 크레인은 가장 큰 박스부터 차례대로 탐색
cranes.sort(reverse=True)
boxes.sort(reverse=True)

answer = 0

while True:
    # 박스 옮기기 전 현재 박스 가져오기
    current_box = boxes[:]

    for crane in cranes:
        idx = 0
        # 가장 큰 박스부터 차례대로 보면서 옮길 수 있으면 옮기기
        for idx in range(len(boxes)):
            if boxes[idx] <= crane:
                # 현재 박스 제외하고 리스트 만들기(슬라이싱으로 시간 단축)
                boxes = boxes[:idx] + boxes[idx+1:]
                break
        # 만약 모든 박스를 다 봤는데도 옮길 수 있는 박스가 없다면, 해당 크레인 지우기
        else:
            cranes.remove(crane)
    answer += 1

    # 박스가 안 남아있으면 종료
    if not boxes:
        break

    # 모든 크레인을 봤는데도 박스 수가 그대로면, -1 출력
    if len(current_box) == len(boxes):
        answer = -1
        break

print(answer)
