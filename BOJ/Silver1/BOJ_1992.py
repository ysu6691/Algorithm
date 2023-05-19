import sys
input = sys.stdin.readline

def find_answer(start_r, start_c, size, is_start, is_end):
    global answer

    if is_start:
        answer += "("

    flag = False
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if arr[r][c] != arr[start_r][start_c]:
                flag = True
                break
        if flag:
            break
    else:
        answer += arr[start_r][start_c]
        if is_end:
            answer += ")"
        return
    
    find_answer(start_r, start_c, size // 2, True, False)
    find_answer(start_r, start_c + size // 2, size // 2, False, False)
    find_answer(start_r + size // 2, start_c, size // 2, False, False)
    find_answer(start_r + size // 2, start_c + size // 2, size // 2, False, True)
    if is_end:
        answer += ")"


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
answer = ""
find_answer(0, 0, N, True, False)
print(answer[1:])