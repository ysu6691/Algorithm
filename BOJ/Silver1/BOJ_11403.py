# 모든 정점에서 DFS 수행

N = int(input())

# 결과를 출력할 함수
arr = [[0]*N for _ in range(N)]

# 인접 행렬(인덱스 1부터 시작하도록 생성)
adj_matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
adj_matrix.insert(0, [0]*(N+1))

# 1부터 N까지 돌면서, 도달할 수 있는 경로 arr에 저장
for i in range(1, N+1):

    stack = [i]
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            # 자기 자신은 일단 visited에 넣지 않음
            if current != i:
                visited.append(current)

            for destination in range(1, N+1):
                if adj_matrix[current][destination] and destination not in visited:
                    stack.append(destination)
                    
                    # 만약 도착지로 다시 자기 자신이 나왔을 경우에는, visited에 추가
                    if destination == i:
                        visited.append(destination)

    # 출발점은 i이고, 도착점들은 visited에 있으므로, arr에 저장 
    for j in range(1, N+1):
        if j in visited:
            arr[i-1][j-1] = 1

for i in range(N):
    print(' '.join(map(str, arr[i])))
