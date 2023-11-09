import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
for i in combinations_with_replacement(range(1, N + 1), M):
    sys.stdout.write(" ".join(map(str, i)) + "\n")
sys.stdout.flush()
