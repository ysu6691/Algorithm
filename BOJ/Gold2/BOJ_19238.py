from collections import deque

# 승객 찾기
def find_customer(queue):
    global fuel

    visited = set()
    customers = []

    # BFS
    while queue:
        cnt = len(queue)
        for _ in range(cnt):
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                # 승객 찾으면 현재 좌표와 승객의 도착지 저장
                if arr[current[0]][current[1]]:
                    customers.append((current[0], current[1], arr[current[0]][current[1]]))

                for i in range(4):
                    nr = current[0] + dr[i]
                    nc = current[1] + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                        if arr[nr][nc] == 1:
                            continue
                        queue.append((nr, nc))

        # 승객을 찾았다면, 승객 중 조건에 맞는 승객의 좌표와 도착지 가져오기
        if customers:
            customers.sort()
            customer_position = (customers[0][0], customers[0][1])
            destination = customers[0][2]
            # 현재 좌표는 0으로
            arr[customer_position[0]][customer_position[1]] = 0
            return customer_position, destination
        # 연료가 없으면 종료
        if not fuel:
            return False, False
        fuel -= 1
    # 승객에 도달하지 못하면 종료
    return False, False


# 승객 도착지로 보내기
def go_to_destination(queue, destination):
    global fuel

    # 승객 태우기 전 연료 저장
    current_fuel = fuel
    flag = False
    visited = set()

    # BFS
    while queue:
        cnt = len(queue)
        for _ in range(cnt):
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                # 도착지 도달했다면 종료
                if current == destination:
                    flag = True
                    break

                for i in range(4):
                    nr = current[0] + dr[i]
                    nc = current[1] + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                        if arr[nr][nc] == 1:
                            continue
                        queue.append((nr, nc))

        # 잘 도착했다면 연료 채우기
        if flag:
            fuel += (current_fuel - fuel) * 2
            return destination
        # 연료 없으면 종료
        if not fuel:
            return False
        fuel -= 1
    # 목적지에 도달하지 못했으면 종료
    return False

########################################################

N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
r -= 1
c -= 1

for _ in range(M):
    cr, cc, dr, dc = map(int, input().split())
    arr[cr-1][cc-1] = (dr-1, dc-1)

queue = deque([(r, c)])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(M):
    # 승객 좌표와 도착지 받아오기
    customer_position, destination = find_customer(queue)
    # 만약 찾지 못했다면 종료
    if not customer_position:
        fuel = -1
        break
    # 승객 좌표 deque로 변환
    queue = deque([customer_position])
    # 도착지 받아오기
    result = go_to_destination(queue, destination)
    # 만약 도착하지 못했다면 종료
    if not result:
        fuel = -1
        break
    # 출발 좌표 deque로 변환
    queue = deque([result])

print(fuel)
