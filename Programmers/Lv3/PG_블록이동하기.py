from collections import deque

def solution(board):        
    
    size = len(board)
    inf = 987654321
    
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    
    queue = deque([(0, 1, 0, 0)])
    memo = [[[inf, inf] for _ in range(size)] for _ in range(size)]
    answer = inf
    
    while queue:
        r, c, mode, time = queue.popleft()
        
        if memo[r][c][mode] <= time:
            continue
        memo[r][c][mode] = time
        
        if (r, c) == (size - 1, size - 1):
            answer = time
            continue
        
        # 이동
        r1 = r + dr[mode]
        c1 = c + dc[mode]
        for i in range(4):
            nr1 = r + dr[i]
            nc1 = c + dc[i]
            nr2 = r1 + dr[i]
            nc2 = c1 + dc[i]
            if 0 <= nr1 < size and 0 <= nc1 < size and 0 <= nr2 < size and 0 <= nc2 < size:
                if not board[nr1][nc1] and not board[nr2][nc2] and memo[nr1][nc1][mode] > time + 1:
                    queue.append((nr1, nc1, mode, time + 1))
    
        # 회전
        if not mode:
            if r - 1 >= 0 and not board[r - 1][c] and not board[r - 1][c - 1]:
                if memo[r][c - 1][1] > time + 1:
                    queue.append((r, c - 1, 1, time + 1))
                if memo[r][c][1] > time + 1:
                    queue.append((r, c, 1, time + 1))
            if r + 1 < size and not board[r + 1][c] and not board[r + 1][c - 1]:
                if memo[r + 1][c - 1][1] > time + 1:
                    queue.append((r + 1, c - 1, 1, time + 1))
                if memo[r + 1][c][1] > time + 1:
                    queue.append((r + 1, c, 1, time + 1))
        else:
            if c - 1 >= 0 and not board[r][c - 1] and not board[r - 1][c - 1]:
                if memo[r - 1][c][0] > time + 1:
                    queue.append((r - 1, c, 0, time + 1))
                if memo[r][c][0] > time + 1:
                    queue.append((r, c, 0, time + 1))
            if c + 1 < size and not board[r][c + 1] and not board[r - 1][c + 1]:
                if memo[r - 1][c + 1][0] > time + 1:
                    queue.append((r - 1, c + 1, 0, time + 1))
                if memo[r][c + 1][0] > time + 1:
                    queue.append((r, c + 1, 0, time + 1))
    
    return min(memo[-1][-1])