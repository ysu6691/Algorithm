import sys
input = sys.stdin.readline

def find_answer(start_r, start_c, size):
    global answer

    flag = False
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if arr[r][c] != arr[start_r][start_c]:
                flag = True
                break
        if flag:
            break
    else:
        answer[arr[start_r][start_c]] += 1
        return
    
    find_answer(start_r, start_c, size // 2)
    find_answer(start_r + size // 2, start_c, size // 2)
    find_answer(start_r, start_c + size // 2, size // 2)
    find_answer(start_r + size // 2, start_c + size // 2, size // 2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]
find_answer(0, 0, N)
print(answer[0])
print(answer[1])
