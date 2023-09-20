import sys
input = sys.stdin.readline

def make_star(r, c, size):
    if size == 3:
        arr[r][c] = "*"
        arr[r + 1][c - 1] = "*"
        arr[r + 1][c + 1] = "*"
        arr[r + 2][c - 2] = "*"
        arr[r + 2][c - 1] = "*"
        arr[r + 2][c] = "*"
        arr[r + 2][c + 1] = "*"
        arr[r + 2][c + 2] = "*"
        return
    
    make_star(r, c, size // 2)
    make_star(r + size // 2, c - size // 2, size // 2)
    make_star(r + size // 2, c + size // 2, size // 2)


N = int(input())
arr = [[" "] * (N * 2 - 1) for _ in range(N)]
make_star(0, N - 1, N)

for r in range(N):
    sys.stdout.write("".join(arr[r]) + "\n")
sys.stdout.flush()
