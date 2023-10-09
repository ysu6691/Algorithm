import sys
input = sys.stdin.readline

def dfs(r, c, cnt):
    global answer

    answer = max(answer, cnt)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and not visited[ord(arr[nr][nc]) - 65]:
            visited[ord(arr[nr][nc]) - 65] = 1
            dfs(nr, nc, cnt + 1)
            visited[ord(arr[nr][nc]) - 65] = 0


R, C = map(int, input().split())
arr = [input() for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [0] * 26
visited[ord(arr[0][0]) - 65] = 1
answer = 0

dfs(0, 0, 1)
print(answer)
