import sys
input = sys.stdin.readline

def find_answer(start_r, start_c, size):
    global answer

    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if arr[r][c] != arr[start_r][start_c]:
                for i in range(0, size, size // 3):
                    for j in range(0, size, size // 3):
                        find_answer(start_r + i, start_c + j, size // 3)
                return
    answer[arr[start_r][start_c]] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = {-1: 0, 0: 0, 1: 0}
find_answer(0, 0, N)

print(answer[-1])
print(answer[0])
print(answer[1])
