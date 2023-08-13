import heapq

def solution(n, start, end, roads, traps):
    
    trap_dict = dict()
    for i in range(len(traps)):
        trap_dict[traps[i]] = i
    
    adj_list = [dict() for _ in range(n + 1)]
    rev_list = [dict() for _ in range(n + 1)]
    for road in roads:
        if road[1] in adj_list[road[0]]:
            adj_list[road[0]][road[1]] = min(road[2], adj_list[road[0]][road[1]])
        else:
            adj_list[road[0]][road[1]] = road[2]
        if road[0] in rev_list[road[1]]:
            rev_list[road[1]][road[0]] = min(road[2], rev_list[road[1]][road[0]])
        else:
            rev_list[road[1]][road[0]] = road[2]
            
    heap = [[0, start, 0]]
    INF = 987654321
    distance = [[INF] * (n + 1) for _ in range(1 << len(traps))]
    
    answer = INF
    while heap:
        acc, current, visited_traps = heapq.heappop(heap)
        if current in trap_dict:
            visited_traps = (1 << trap_dict[current]) ^ visited_traps
        
        if distance[visited_traps][current] <= acc:
            continue
        distance[visited_traps][current] = acc
        
        if current == end:
            answer = min(answer, acc)
            continue
            
        if current in trap_dict and (1 << trap_dict[current]) & visited_traps:
            for adj_node in rev_list[current].keys():
                cost = rev_list[current][adj_node]
                if adj_node in trap_dict and visited_traps & (1 << trap_dict[adj_node]):
                    continue
                if distance[visited_traps][adj_node] > acc + cost:
                    heapq.heappush(heap, (acc + cost, adj_node, visited_traps))
            for adj_node in adj_list[current].keys():
                cost = adj_list[current][adj_node]
                if adj_node in trap_dict and visited_traps & (1 << trap_dict[adj_node]):
                    if distance[visited_traps ^ (1 << trap_dict[adj_node])][adj_node] > acc + cost:
                        heapq.heappush(heap, (acc + cost, adj_node, visited_traps))
            continue
            
        for adj_node in adj_list[current].keys():
            cost = adj_list[current][adj_node]
            if adj_node in trap_dict and visited_traps & (1 << trap_dict[adj_node]):
                continue
            if distance[visited_traps][adj_node] > acc + cost:
                heapq.heappush(heap, (acc + cost, adj_node, visited_traps))
        for adj_node in rev_list[current].keys():
            cost = rev_list[current][adj_node]
            if adj_node in trap_dict and visited_traps & (1 << trap_dict[adj_node]):
                if distance[visited_traps ^ (1 << trap_dict[adj_node])][adj_node] > acc + cost:
                    heapq.heappush(heap, (acc + cost, adj_node, visited_traps))
    
    return answer