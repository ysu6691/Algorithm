def solution(info, edges):
    
    def dfs(current, candidates, acc, sheeps):
        nonlocal answer
        
        # 현재 노드가 양인지 늑대인지 확인
        if not info[current]:
            acc += 1
            sheeps += 1
        else:
            acc -= 1
            if acc <= 0:
                if sheeps > answer:
                    answer = sheeps
                return
        
        # 갈 수 있는 후보 노드 갱신
        candidates = candidates[:]
        candidates.remove(current)
        for child in children[current]:
            candidates.append(child)
            
        # 갈 수 있는 노드가 없는 경우
        if not candidates:
            if sheeps > answer:
                answer = sheeps
            return
        
        # 다음 노드로
        for candidate in candidates:
            dfs(candidate, candidates, acc, sheeps)
    
    children = [[] for _ in range(len(info))]
    for edge in edges:
        n1, n2 = edge[0], edge[1]
        children[n1].append(n2)
    
    answer = 0
    dfs(0, [0], 0, 0)
    
    return answer