testcase = int(input())

for tc in range(1, testcase+1):

    N = int(input())

    station_dict = {}

    for i in range(N):
        bus, A, B = map(int, input().split())

        station_list = [A, B]

        for j in range(A+1, B):
            if bus == 1:
                station_list.append(j)
            elif bus == 2:
                if A % 2:
                    if j % 2:
                        station_list.append(j)
                else:
                    if not (j % 2):
                        station_list.append(j)
            elif bus == 3:
                if A % 2:
                    if not (j % 3) and (j % 10):
                        station_list.append(j)
                else:
                    if not (j % 4):
                        station_list.append(j)

        for station in station_list:
            if station_dict.get(station, -1) == -1:
                station_dict[station] = 1
            else:
                station_dict[station] += 1

    print(f'#{tc} {max(station_dict.values())}')